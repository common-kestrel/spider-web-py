import pytest
from assertpy import assert_that
from typing import Tuple, List, Any
from spider_web import SpiderWeb, SpiderWebNode


def assert_common_properties_add(spider_web, values, index=0, level=0) -> None:
    assert_that(spider_web.size()).is_equal_to(len(values))
    assert_that(spider_web.get_first_node()).is_not_none()
    assert_that(spider_web.get_last_node()).is_not_none()
    assert_that(spider_web.get_prev_level()).is_none()
    assert_that(spider_web.get_first()).is_equal_to(values[0])
    assert_that(spider_web.get_last()).is_equal_to(values[-1])
    assert_that(spider_web.get_index()).is_equal_to(index)
    assert_that(spider_web.get_level()).is_equal_to(level)


def assert_common_properties_add_node(spider_web: SpiderWeb, nodes: list, index: int = 0, level: int = 0) -> None:
    values = [node.get_value() for node in nodes]
    assert_common_properties_add(spider_web, values, index, level)


@pytest.fixture(scope="function")
def spider_web_default_max_element() -> SpiderWeb:
    """
    Fixture for creating a SpiderWeb instance with the default max_element_per_level (6).
    """
    return SpiderWeb()


@pytest.fixture(scope="function")
def spider_web_custom_max_element() -> SpiderWeb:
    """
    Fixture for creating a SpiderWeb instance with a custom max_element_per_level (3).
    """
    return SpiderWeb(max_element_per_level=3)


@pytest.fixture(scope="function")
def spider_web_with_values() -> SpiderWeb:
    """
    Fixture for creating a SpiderWeb instance with values [0, 1, 2, 3, 4, 1, 2, 3].
    """
    spider_web = SpiderWeb(max_element_per_level=3)
    values = [value for value in [0, 1, 2, 3, 4, 1, 2, 3]]
    for value in values:
        spider_web.add(value)
    return spider_web


@pytest.fixture(scope="function")
def spider_web_with_nodes() -> Tuple[SpiderWeb, List[SpiderWebNode]]:
    """
    Fixture for creating a SpiderWeb instance with nodes [0, 1, 2, 3, 4, 1, 2, 3].
    """
    spider_web = SpiderWeb(max_element_per_level=3)
    nodes = [SpiderWebNode(value) for value in [0, 1, 2, 3, 4, 1, 2, 3]]
    for node in nodes:
        spider_web.add(node)
    return spider_web, nodes


@pytest.mark.spider_web
def test_get_first_node_empty_spider_web(spider_web_default_max_element: SpiderWeb) -> None:
    """
    Test if the get_first_node method returns None for an empty SpiderWeb.
    """
    result = spider_web_default_max_element.get_first_node()
    assert_that(result).is_none()


@pytest.mark.spider_web
def test_get_first_node_non_empty_spider_web(spider_web_custom_max_element: SpiderWeb) -> None:
    """
    Test if the get_first_node method returns the correct first node for a non-empty SpiderWeb.
    """
    spider_web_custom_max_element._first = SpiderWebNode(value="first_node_value")

    result = spider_web_custom_max_element.get_first_node()
    assert_that(result).is_instance_of(SpiderWebNode)
    assert_that(result.get_value()).is_equal_to("first_node_value")


@pytest.mark.spider_web
def test_get_prev_level_empty_spider_web(spider_web_default_max_element: SpiderWeb) -> None:
    """
    Test if the get_prev_level method returns None for an empty SpiderWeb.
    """
    result = spider_web_default_max_element.get_prev_level()
    assert_that(result).is_none()


@pytest.mark.spider_web
def test_get_prev_level_non_empty_spider_web(spider_web_default_max_element: SpiderWeb):
    """
    Test if the get_prev_level method returns the correct previous level node for a non-empty SpiderWeb.
    """
    spider_web_default_max_element._prev_level = SpiderWebNode(value="prev_level_node_value")

    result = spider_web_default_max_element.get_prev_level()
    assert_that(result).is_instance_of(SpiderWebNode)
    assert_that(result.get_value()).is_equal_to("prev_level_node_value")


@pytest.mark.spider_web
def test_get_last_node_empty_spider_web(spider_web_default_max_element: SpiderWeb) -> None:
    """
    Test if the get_last_node method returns None for an empty SpiderWeb.
    """
    result = spider_web_default_max_element.get_last_node()
    assert_that(result).is_none()


@pytest.mark.spider_web
def test_get_last_node_non_empty_spider_web(spider_web_default_max_element: SpiderWeb) -> None:
    """
    Test if the get_last_node method returns the correct last node for a non-empty SpiderWeb.
    """
    # Assuming SpiderWebNode has an __init__ method that takes a value parameter
    spider_web_default_max_element._last = SpiderWebNode(value="last_node_value")

    result = spider_web_default_max_element.get_last_node()
    assert_that(result).is_instance_of(SpiderWebNode)
    assert_that(result.get_value()).is_equal_to("last_node_value")


@pytest.mark.parametrize("element_count, expected_level", [
        (0, -1),
        (1, 0),
        (3, 0),
        (4, 1),
        (6, 1),
        (7, 2),
        (10, 3)
    ]
)
@pytest.mark.spider_web
def test_get_level(spider_web_custom_max_element: SpiderWeb, element_count: int, expected_level: int) -> None:
    """
    Parametrized test for the get_level method in SpiderWeb.

    :param element_count: The number of elements to add to the SpiderWeb.
    :param expected_level: The expected level for the SpiderWeb.
    """
    for i in range(element_count):
        spider_web_custom_max_element.add(i)

    result = spider_web_custom_max_element.get_level()
    assert_that(result).is_equal_to(expected_level)


@pytest.mark.parametrize("elements, expected_size", [
    ([], 0),
    ([1, 2, 3], 3),
    (["a", 2, "c", 4, 5], 5),
    ([0, 1, 2, 3, 4, 5], 6)
])
@pytest.mark.spider_web
def test_size(spider_web_custom_max_element: SpiderWeb, elements: list, expected_size: int) -> None:
    """
    Parametrized test for the size method in SpiderWeb.

    :param elements: List of elements to add to the SpiderWeb.
    :param expected_size: The expected size for the SpiderWeb.
    """
    for element in elements:
        spider_web_custom_max_element.add(element)

    result = spider_web_custom_max_element.size()
    assert_that(result).is_equal_to(expected_size)


@pytest.mark.parametrize("element_count, level, expected_index", [
    (0, 0, ValueError),
    (0, 1, ValueError),
    (1, -1, ValueError),
    (3, 1, ValueError),
    (4, 0, 2),
    (4, 1, 0),
    (4, 2, ValueError),
    (8, 1, 2),
    (8, 2, 1)
])
@pytest.mark.spider_web
def test_get_maximum_index_for_level(
        spider_web_custom_max_element: SpiderWeb,
        element_count: int,
        level: int,
        expected_index: int
) -> None:
    """
    Parametrized test for the get_maximum_index_for_level method in SpiderWeb.

    :param element_count: The number of elements to add to the SpiderWeb.
    :param level: The level for which to retrieve the maximum index.
    :param expected_index: The expected maximum index for the specified level.
    """
    for i in range(element_count):
        spider_web_custom_max_element.add(i)

    if expected_index == ValueError:
        with pytest.raises(ValueError):
            spider_web_custom_max_element.get_maximum_index_for_level(level)
    else:
        result = spider_web_custom_max_element.get_maximum_index_for_level(level)
        assert_that(result).is_equal_to(expected_index)


@pytest.mark.spider_web
def test_print_empty_spider_web(capsys, spider_web_default_max_element: SpiderWeb) -> None:
    """
    Test the print method for an empty SpiderWeb.
    """
    spider_web_default_max_element.print()
    captured = capsys.readouterr()
    assert_that(captured.out).is_empty()


@pytest.mark.spider_web
def test_print_non_empty_spider_web(capsys, spider_web_custom_max_element: SpiderWeb) -> None:
    """
    Test the print method for a non-empty SpiderWeb.
    """
    for i in range(7):
        spider_web_custom_max_element.add(i)

    spider_web_custom_max_element.print()
    captured = capsys.readouterr()

    expected_output = ("level: 0, index: 0, value: 0\n"
                       "level: 0, index: 1, value: 1\n"
                       "level: 0, index: 2, value: 2\n"
                       "level: 1, index: 0, value: 3\n"
                       "level: 1, index: 1, value: 4\n"
                       "level: 1, index: 2, value: 5\n"
                       "level: 2, index: 0, value: 6\n")
    assert_that(captured.out).is_equal_to(expected_output)


@pytest.mark.spider_web
def test_add_element_to_empty_spider_web(spider_web_default_max_element: SpiderWeb) -> None:
    """
    Test adding an element to an empty SpiderWeb.
    """
    spider_web_default_max_element.add("value")

    assert_common_properties_add(spider_web_default_max_element, ["value"])
    (assert_that(spider_web_default_max_element.get_first_node()).
     is_equal_to(spider_web_default_max_element.get_last_node()))


@pytest.mark.spider_web
def test_add_element_to_non_empty_spider_web(spider_web_default_max_element: SpiderWeb) -> None:
    """
    Test adding an element to a non-empty SpiderWeb.
    """
    values = ["value1", "value2"]
    for value in values:
        spider_web_default_max_element.add(value)

    assert_common_properties_add(spider_web_default_max_element, values, index=1, level=0)
    (assert_that(spider_web_default_max_element.get_first_node()).
     is_not_equal_to(spider_web_default_max_element.get_last_node()))
    (assert_that(spider_web_default_max_element.get_first_node().get_next_node()).
     is_equal_to(spider_web_default_max_element.get_last_node()))
    (assert_that(spider_web_default_max_element.get_last_node().get_prev_node()).
     is_equal_to(spider_web_default_max_element.get_first_node()))


@pytest.mark.spider_web
def test_add_node_to_empty_spider_web(spider_web_default_max_element: SpiderWeb) -> None:
    """
    Test adding a SpiderWebNode to an empty SpiderWeb.
    """

    node = SpiderWebNode("value")
    spider_web_default_max_element.add(node)

    assert_common_properties_add_node(spider_web_default_max_element, [node])
    (assert_that(spider_web_default_max_element.get_first_node()).
     is_equal_to(spider_web_default_max_element.get_last_node()))


@pytest.mark.spider_web
def test_add_node_to_non_empty_spider_web(spider_web_default_max_element: SpiderWeb) -> None:
    """
    Test adding a SpiderWebNode to a non-empty SpiderWeb.
    """
    nodes = [SpiderWebNode("value1"), SpiderWebNode("value2")]
    for node in nodes:
        spider_web_default_max_element.add(node)

    assert_common_properties_add_node(spider_web_default_max_element, nodes, index=1, level=0)
    (assert_that(spider_web_default_max_element.get_first_node()).
     is_not_equal_to(spider_web_default_max_element.get_last_node()))
    (assert_that(spider_web_default_max_element.get_first_node().get_next_node()).
     is_equal_to(spider_web_default_max_element.get_last_node()))
    (assert_that(spider_web_default_max_element.get_last_node().get_prev_node()).
     is_equal_to(spider_web_default_max_element.get_first_node()))


@pytest.mark.spider_web
def test_add_first_element_to_empty_spider_web(spider_web_default_max_element: SpiderWeb) -> None:
    """
    Test adding an element to the beginning of an empty SpiderWeb.
    """
    spider_web_default_max_element.add_first("value")

    assert_common_properties_add(spider_web_default_max_element, ["value"])
    (assert_that(spider_web_default_max_element.get_first_node()).
     is_equal_to(spider_web_default_max_element.get_last_node()))


@pytest.mark.spider_web
def test_add_first_element_to_non_empty_spider_web(spider_web_default_max_element: SpiderWeb) -> None:
    """
    Test adding an element to the beginning of a non-empty SpiderWeb.
    """
    values = ["value1", "value2"]
    for value in values:
        spider_web_default_max_element.add_first(value)
    values.reverse()

    assert_common_properties_add(spider_web_default_max_element, values, index=1, level=0)

    (assert_that(spider_web_default_max_element.get_first_node()).
     is_not_equal_to(spider_web_default_max_element.get_last_node()))
    (assert_that(spider_web_default_max_element.get_first_node().get_next_node()).
     is_equal_to(spider_web_default_max_element.get_last_node()))
    (assert_that(spider_web_default_max_element.get_last_node().get_prev_node()).
     is_equal_to(spider_web_default_max_element.get_first_node()))


@pytest.mark.spider_web
def test_add_first_node_to_empty_spider_web(spider_web_default_max_element: SpiderWeb) -> None:
    """
    Test adding a SpiderWebNode to the beginning of an empty SpiderWeb.
    """
    node = SpiderWebNode("value")
    spider_web_default_max_element.add_first(node)

    assert_common_properties_add_node(spider_web_default_max_element, [node])
    (assert_that(spider_web_default_max_element.get_first_node()).
     is_equal_to(spider_web_default_max_element.get_last_node()))


@pytest.mark.spider_web
def test_add_first_node_to_non_empty_spider_web(spider_web_default_max_element: SpiderWeb) -> None:
    """
    Test adding a SpiderWebNode to the beginning of a non-empty SpiderWeb.
    """
    nodes = [SpiderWebNode("value1"), SpiderWebNode("value2")]
    for node in nodes:
        spider_web_default_max_element.add_first(node)
    nodes.reverse()

    assert_common_properties_add_node(spider_web_default_max_element, nodes, index=1, level=0)
    (assert_that(spider_web_default_max_element.get_first_node()).
     is_not_equal_to(spider_web_default_max_element.get_last_node()))
    (assert_that(spider_web_default_max_element.get_first_node().get_next_node()).
     is_equal_to(spider_web_default_max_element.get_last_node()))
    (assert_that(spider_web_default_max_element.get_last_node().get_prev_node()).
     is_equal_to(spider_web_default_max_element.get_first_node()))


@pytest.mark.spider_web
def test_add_last_element_to_empty_spider_web(spider_web_default_max_element: SpiderWeb) -> None:
    """
    Test adding an element to the end of an empty SpiderWeb.
    """
    spider_web_default_max_element.add_last("value")

    assert_common_properties_add(spider_web_default_max_element, ["value"])
    (assert_that(spider_web_default_max_element.get_first_node()).
     is_equal_to(spider_web_default_max_element.get_last_node()))


@pytest.mark.spider_web
def test_add_last_element_to_non_empty_spider_web(spider_web_default_max_element: SpiderWeb) -> None:
    """
    Test adding an element to the end of a non-empty SpiderWeb.
    """
    values = ["value1", "value2"]
    for value in values:
        spider_web_default_max_element.add(value)

    assert_common_properties_add(spider_web_default_max_element, values, index=1, level=0)
    (assert_that(spider_web_default_max_element.get_first_node()).
     is_not_equal_to(spider_web_default_max_element.get_last_node()))
    (assert_that(spider_web_default_max_element.get_first_node().get_next_node()).
     is_equal_to(spider_web_default_max_element.get_last_node()))
    (assert_that(spider_web_default_max_element.get_last_node().get_prev_node()).
     is_equal_to(spider_web_default_max_element.get_first_node()))


@pytest.mark.spider_web
def test_add_last_node_to_empty_spider_web(spider_web_default_max_element: SpiderWeb) -> None:
    """
    Test adding a SpiderWebNode to the end of an empty SpiderWeb.
    """
    node = SpiderWebNode("value")
    spider_web_default_max_element.add(node)

    assert_common_properties_add_node(spider_web_default_max_element, [node])
    (assert_that(spider_web_default_max_element.get_first_node()).
     is_equal_to(spider_web_default_max_element.get_last_node()))


@pytest.mark.spider_web
def test_add_last_node_to_non_empty_spider_web(spider_web_default_max_element: SpiderWeb) -> None:
    """
    Test adding a SpiderWebNode to the end of a non-empty SpiderWeb.
    """
    nodes = [SpiderWebNode("value1"), SpiderWebNode("value2")]
    for node in nodes:
        spider_web_default_max_element.add(node)

    assert_common_properties_add_node(spider_web_default_max_element, nodes, index=1, level=0)
    (assert_that(spider_web_default_max_element.get_first_node()).
     is_not_equal_to(spider_web_default_max_element.get_last_node()))
    (assert_that(spider_web_default_max_element.get_first_node().get_next_node()).
     is_equal_to(spider_web_default_max_element.get_last_node()))
    (assert_that(spider_web_default_max_element.get_last_node().get_prev_node()).
     is_equal_to(spider_web_default_max_element.get_first_node()))


@pytest.mark.parametrize("value, expected_level, expected_index", [
    (0, 0, 0),
    (1, 0, 1),
    (4, 1, 1)
])
@pytest.mark.spider_web
def test_index_of_element_in_spider_web(
        spider_web_with_values: SpiderWeb,
        value: int,
        expected_level: int,
        expected_index: int
) -> None:
    """
    Parametrized test for the index_of method in SpiderWeb.

    :param value: The element to search for in the SpiderWeb.
    :param expected_level: The expected level of the found element in the SpiderWeb.
    :param expected_index: The expected index of the found element in the SpiderWeb.
    """
    result = spider_web_with_values.index_of(value)
    assert_that(result).is_equal_to({"level": expected_level, "index": expected_index})


@pytest.mark.spider_web
def test_index_of_node_in_spider_web(spider_web_with_nodes: Tuple[SpiderWeb, List[SpiderWebNode]]) -> None:
    """
    Test the index_of method for finding a node in the SpiderWeb.
    """
    spider_web, nodes = spider_web_with_nodes
    result = spider_web.index_of(node=nodes[1])
    assert_that(result).is_equal_to({"level": 0, "index": 1})


@pytest.mark.spider_web
def test_index_of_element_not_in_spider_web(spider_web_with_values: SpiderWeb) -> None:
    """
    Test the index_of method when the element is not present in the SpiderWeb.
    """
    result = spider_web_with_values.index_of(10)
    assert_that(result).is_equal_to({"level": None, "index": None})


@pytest.mark.spider_web
def test_index_of_node_not_in_spider_web(spider_web_with_nodes: Tuple[SpiderWeb, List[SpiderWebNode]]) -> None:
    """
    Test the index_of method when the node is not present in the SpiderWeb.
    """
    spider_web, nodes = spider_web_with_nodes
    new_node = SpiderWebNode(10)
    result = spider_web.index_of(node=new_node)
    assert_that(result).is_equal_to({"level": None, "index": None})


@pytest.mark.parametrize("value, expected_level, expected_index", [
    (0, 0, 0),
    (1, 1, 2),
    (3, 2, 1),
    (4, 1, 1)
])
@pytest.mark.spider_web
def test_last_index_of_element_in_spider_web(
        spider_web_with_values: SpiderWeb,
        value: int,
        expected_level: int,
        expected_index: int
) -> None:
    """
    Parametrized test for the last_index_of method in SpiderWeb.

    :param value: The element to search for in the SpiderWeb.
    :param expected_level: The expected level of the last occurrence in the SpiderWeb.
    :param expected_index: The expected index of the last occurrence in the SpiderWeb.
    """
    result = spider_web_with_values.last_index_of(value)
    assert_that(result).is_equal_to({"level": expected_level, "index": expected_index})


@pytest.mark.spider_web
def test_last_index_of_node_in_spider_web(spider_web_with_nodes: Tuple[SpiderWeb, List[SpiderWebNode]]) -> None:
    """
    Test the last_index_of method for finding the last occurrence of a node in the SpiderWeb.
    """
    spider_web, nodes = spider_web_with_nodes
    result = spider_web.last_index_of(node=nodes[1])
    assert_that(result).is_equal_to({"level": 0, "index": 1})


@pytest.mark.spider_web
def test_last_index_of_element_not_in_spider_web(spider_web_with_values: SpiderWeb) -> None:
    """
    Test the last_index_of method when the element is not present in the SpiderWeb.
    """
    result = spider_web_with_values.last_index_of(10)
    assert_that(result).is_equal_to({"level": None, "index": None})


@pytest.mark.spider_web
def test_last_index_of_node_not_in_spider_web(spider_web_with_nodes: Tuple[SpiderWeb, List[SpiderWebNode]]) -> None:
    """
    Test the last_index_of method when the node is not present in the SpiderWeb.
    """
    spider_web, nodes = spider_web_with_nodes
    new_node = SpiderWebNode(10)
    result = spider_web.last_index_of(node=new_node)
    assert_that(result).is_equal_to({"level": None, "index": None})


@pytest.mark.parametrize("level, index, expected_value", [
    (0, 0, 0),
    (0, 2, 2),
    (1, 0, 3),
    (2, 1, 3),
    (-1, 0, ValueError),
    (0, -1, ValueError),
    (0, 3, ValueError),
    (2, 2, ValueError)
])
@pytest.mark.spider_web
def test_get(spider_web_with_values: SpiderWeb, level: int, index: int, expected_value: int) -> None:
    """
    Test the get method with valid parameters.

    :param spider_web_with_values: An instance of the SpiderWeb class with pre-set values.
    :param level: The level of the element to retrieve.
    :param index: The index within the specified level to retrieve.
    :param expected_value: The expected value or ValueError if an error is expected.
    """
    if expected_value == ValueError:
        with pytest.raises(ValueError):
            spider_web_with_values.get(level=level, index=index)
    else:
        result = spider_web_with_values.get(level=level, index=index)
        assert_that(result).is_equal_to(expected_value)


@pytest.mark.parametrize("level, index, expected_value", [
    (0, 0, 0),
    (0, 2, 2),
    (1, 0, 3),
    (2, 1, 3),
    (-1, 0, ValueError),
    (0, -1, ValueError),
    (0, 3, ValueError),
    (2, 2, ValueError)
])
@pytest.mark.spider_web
def test_get_node(spider_web_with_values: SpiderWeb, level: int, index: int, expected_value: int) -> None:
    """
        Test the get method with valid parameters.

        :param spider_web_with_values: An instance of the SpiderWeb class with pre-set values.
        :param level: The level of the SpiderWebNode to retrieve.
        :param index: The index within the specified level to retrieve.
        :param expected_value: The expected value or ValueError if an error is expected.
        """
    if expected_value == ValueError:
        with pytest.raises(ValueError):
            spider_web_with_values.get_node(level=level, index=index)
    else:
        result: SpiderWebNode = spider_web_with_values.get_node(level=level, index=index)
        assert_that(result.get_value()).is_equal_to(expected_value)


@pytest.mark.parametrize("level, index, new_value, expected_old_value", [
    (0, 0, 10, 0),
    (0, 2, 2, 2),
    (1, 0, 20, 3),
    (2, 1, 30, 3),
    (-1, 0, 10, ValueError),
    (0, -1, 20, ValueError),
    (0, 3, 30, ValueError),
    (2, 2, 40, ValueError)
])
@pytest.mark.spider_web
def test_set(spider_web_with_values: SpiderWeb, level: int, index: int, new_value: int, expected_old_value: int) -> None:
    """
    Test the get method with valid parameters.

    :param spider_web_with_values: An instance of the SpiderWeb class with pre-set values.
    :param level: The level at which to set the element.
    :param index: The index within the specified level to set the element.
    :param new_value: The new value to be set at the specified level and index.
    :param expected_old_value: The expected old value at the specified level and index.
    """
    if expected_old_value == ValueError:
        with pytest.raises(ValueError):
            spider_web_with_values.set(level=level, index=index, element=new_value)
    else:
        result = spider_web_with_values.set(level=level, index=index, element=new_value)
        assert_that(result).is_equal_to(expected_old_value)
        assert_that(spider_web_with_values.get(level=level, index=index)).is_equal_to(new_value)


@pytest.mark.parametrize("initial_elements, expected_first_value, expected_size, expected_new_first_value", [
    ([], IndexError, 0, None),
    ([1], 1, 0, IndexError),
    ([1, 2, 3], 1, 2, 2),
    (["a", "b", 3, 4], "a", 3, "b")
])
@pytest.mark.spider_web
def test_remove_first(
        spider_web_custom_max_element: SpiderWeb,
        initial_elements: list,
        expected_first_value: Any,
        expected_size: int,
        expected_new_first_value: Any
) -> None:
    """
    Test the remove_first method in SpiderWeb.

    :param spider_web_custom_max_element: An instance of the SpiderWeb class with custom maximum element count.
    :param initial_elements: List of elements to initialize the SpiderWeb.
    :param expected_first_value: The expected value of the first element after removal.
    :param expected_size: The expected size of the SpiderWeb after removal.
    :param expected_new_first_value: The expected value of the new first element after removal.
    """
    for element in initial_elements:
        spider_web_custom_max_element.add(element)

    if expected_first_value == IndexError:
        with pytest.raises(IndexError):
            spider_web_custom_max_element.remove_first()
    else:
        result = spider_web_custom_max_element.remove_first()
        assert_that(result).is_equal_to(expected_first_value)
        assert_that(spider_web_custom_max_element.size()).is_equal_to(expected_size)
        if expected_new_first_value == IndexError:
            with pytest.raises(IndexError):
                spider_web_custom_max_element.get_first()
        else:
            assert_that(spider_web_custom_max_element.get_first()).is_equal_to(expected_new_first_value)


@pytest.mark.parametrize("initial_elements, expected_last_value, expected_size, expected_new_last_value", [
    ([], IndexError, 0, None),
    ([1], 1, 0, IndexError),
    ([1, 2, 3], 3, 2, 2),
    (["a", "b", "c", 4], 4, 3, "c")
])
@pytest.mark.spider_web
def test_remove_last(
        spider_web_custom_max_element: SpiderWeb,
        initial_elements: list,
        expected_last_value: Any,
        expected_size: int,
        expected_new_last_value: Any
) -> None:
    """
    Test the remove_first method in SpiderWeb.

    :param spider_web_custom_max_element: An instance of the SpiderWeb class with custom maximum element count.
    :param initial_elements: List of elements to initialize the SpiderWeb.
    :param expected_last_value: The expected value of the last element after removal.
    :param expected_size: The expected size of the SpiderWeb after removal.
    :param expected_new_last_value: The expected value of the new last element after removal.
    """
    for element in initial_elements:
        spider_web_custom_max_element.add(element)

    if expected_last_value == IndexError:
        with pytest.raises(IndexError):
            spider_web_custom_max_element.remove_last()
    else:
        result = spider_web_custom_max_element.remove_last()
        assert_that(result).is_equal_to(expected_last_value)
        assert_that(spider_web_custom_max_element.size()).is_equal_to(expected_size)
        if expected_new_last_value == IndexError:
            with pytest.raises(IndexError):
                spider_web_custom_max_element.get_last()
        else:
            assert_that(spider_web_custom_max_element.get_last()).is_equal_to(expected_new_last_value)


@pytest.mark.parametrize("initial_elements", [
    ([1, 2, 3]),
    ([])
])
@pytest.mark.spider_web
def test_clear_method(spider_web_default_max_element: SpiderWeb, initial_elements) -> None:
    """
    Test the clear method in SpiderWeb.

    :param initial_elements: List of elements to initialize the SpiderWeb.
    """
    for element in initial_elements:
        spider_web_default_max_element.add(element)

    spider_web_default_max_element.clear()

    assert_that(spider_web_default_max_element).is_empty()
    assert_that(spider_web_default_max_element.get_first_node()).is_none()
    assert_that(spider_web_default_max_element.get_last_node()).is_none()
    assert_that(spider_web_default_max_element.get_prev_level()).is_none()


@pytest.mark.spider_web
def test_copy_empty_spider_web(spider_web_custom_max_element: SpiderWeb) -> None:
    """
    Test the copy method on an empty SpiderWeb.
    """
    copied_spider_web = spider_web_custom_max_element.copy()

    assert_that(copied_spider_web).is_empty()
    assert_that(id(spider_web_custom_max_element)).is_not_equal_to(id(copied_spider_web))


@pytest.mark.spider_web
def test_copy_non_empty_spider_web(spider_web_with_values: SpiderWeb) -> None:
    """
    Test the copy method on a non-empty SpiderWeb.
    """
    copied_spider_web = spider_web_with_values.copy()

    assert_that(copied_spider_web.size()).is_equal_to(spider_web_with_values.size())
    assert_that(id(spider_web_with_values)).is_not_equal_to(id(copied_spider_web))
    while copied_spider_web.get_first_node() is not None:
        copied_first_node = copied_spider_web.get_first_node()
        spider_web_first_node = spider_web_with_values.get_first_node()
        assert_that(id(spider_web_first_node)).is_not_equal_to(id(copied_first_node))
        assert_that(spider_web_first_node.get_value()).is_equal_to(copied_first_node.get_value())
        copied_spider_web.remove_first()
        spider_web_with_values.remove_first()

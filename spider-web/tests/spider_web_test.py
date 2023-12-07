import pytest
from assertpy import assert_that
from typing import Tuple, List
from spider_web import SpiderWeb, SpiderWebNode


def assert_common_properties_add(spiderweb, values, index=0, level=0) -> None:
    assert_that(spiderweb.size()).is_equal_to(len(values))
    assert_that(spiderweb.get_first_node()).is_not_none()
    assert_that(spiderweb.get_last_node()).is_not_none()
    assert_that(spiderweb.get_prev_level()).is_none()
    assert_that(spiderweb.get_first()).is_equal_to(values[0])
    assert_that(spiderweb.get_last()).is_equal_to(values[-1])
    assert_that(spiderweb.get_index()).is_equal_to(index)
    assert_that(spiderweb.get_level()).is_equal_to(level)


def assert_common_properties_add_node(spiderweb: SpiderWeb, nodes: list, index: int = 0, level: int = 0) -> None:
    values = [node.get_value() for node in nodes]
    assert_common_properties_add(spiderweb, values, index, level)


@pytest.fixture(scope="function")
def spiderweb_default_max_element() -> SpiderWeb:
    """
    Fixture for creating a SpiderWeb instance with the default max_element_per_level (6).
    """
    return SpiderWeb()


@pytest.fixture(scope="function")
def spiderweb_custom_max_element() -> SpiderWeb:
    """
    Fixture for creating a SpiderWeb instance with a custom max_element_per_level (3).
    """
    return SpiderWeb(max_element_per_level=3)


@pytest.fixture(scope="function")
def spiderweb_with_values() -> SpiderWeb:
    """
    Fixture for creating a SpiderWeb instance with values [0, 1, 2, 3, 4, 1, 2, 3].
    """
    spiderweb = SpiderWeb(max_element_per_level=3)
    values = [value for value in [0, 1, 2, 3, 4, 1, 2, 3]]
    for value in values:
        spiderweb.add(value)
    return spiderweb


@pytest.fixture(scope="function")
def spiderweb_with_nodes() -> Tuple[SpiderWeb, List[SpiderWebNode]]:
    """
    Fixture for creating a SpiderWeb instance with nodes [0, 1, 2, 3, 4, 1, 2, 3].
    """
    spiderweb = SpiderWeb(max_element_per_level=3)
    nodes = [SpiderWebNode(value) for value in [0, 1, 2, 3, 4, 1, 2, 3]]
    for node in nodes:
        spiderweb.add(node)
    return spiderweb, nodes


@pytest.mark.spider_web
def test_get_first_node_empty_spiderweb(spiderweb_default_max_element: SpiderWeb) -> None:
    """
    Test if the get_first_node method returns None for an empty SpiderWeb.
    """
    result = spiderweb_default_max_element.get_first_node()
    assert_that(result).is_none()


@pytest.mark.spider_web
def test_get_first_node_non_empty_spiderweb(spiderweb_custom_max_element: SpiderWeb) -> None:
    """
    Test if the get_first_node method returns the correct first node for a non-empty SpiderWeb.
    """
    spiderweb_custom_max_element._first = SpiderWebNode(value="first_node_value")

    result = spiderweb_custom_max_element.get_first_node()
    assert_that(result).is_instance_of(SpiderWebNode)
    assert_that(result.get_value()).is_equal_to("first_node_value")


@pytest.mark.spider_web
def test_get_prev_level_empty_spiderweb(spiderweb_default_max_element: SpiderWeb) -> None:
    """
    Test if the get_prev_level method returns None for an empty SpiderWeb.
    """
    result = spiderweb_default_max_element.get_prev_level()
    assert_that(result).is_none()


@pytest.mark.spider_web
def test_get_prev_level_non_empty_spiderweb(spiderweb_default_max_element: SpiderWeb):
    """
    Test if the get_prev_level method returns the correct previous level node for a non-empty SpiderWeb.
    """
    spiderweb_default_max_element._prev_level = SpiderWebNode(value="prev_level_node_value")

    result = spiderweb_default_max_element.get_prev_level()
    assert_that(result).is_instance_of(SpiderWebNode)
    assert_that(result.get_value()).is_equal_to("prev_level_node_value")


@pytest.mark.spider_web
def test_get_last_node_empty_spiderweb(spiderweb_default_max_element: SpiderWeb) -> None:
    """
    Test if the get_last_node method returns None for an empty SpiderWeb.
    """
    result = spiderweb_default_max_element.get_last_node()
    assert_that(result).is_none()


@pytest.mark.spider_web
def test_get_last_node_non_empty_spiderweb(spiderweb_default_max_element: SpiderWeb) -> None:
    """
    Test if the get_last_node method returns the correct last node for a non-empty SpiderWeb.
    """
    # Assuming SpiderWebNode has an __init__ method that takes a value parameter
    spiderweb_default_max_element._last = SpiderWebNode(value="last_node_value")

    result = spiderweb_default_max_element.get_last_node()
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
def test_get_level(spiderweb_custom_max_element: SpiderWeb, element_count: int, expected_level: int) -> None:
    """
    Parametrized test for the get_level method in SpiderWeb.

    :param element_count: The number of elements to add to the SpiderWeb.
    :param expected_level: The expected level for the SpiderWeb.
    """
    for i in range(element_count):
        spiderweb_custom_max_element.add(i)

    result = spiderweb_custom_max_element.get_level()
    assert_that(result).is_equal_to(expected_level)


@pytest.mark.parametrize("elements, expected_size", [
    ([], 0),
    ([1, 2, 3], 3),
    (["a", 2, "c", 4, 5], 5),
    ([0, 1, 2, 3, 4, 5], 6)
])
@pytest.mark.spider_web
def test_size(spiderweb_custom_max_element: SpiderWeb, elements: list, expected_size: int) -> None:
    """
    Parametrized test for the size method in SpiderWeb.

    :param elements: List of elements to add to the SpiderWeb.
    :param expected_size: The expected size for the SpiderWeb.
    """
    for element in elements:
        spiderweb_custom_max_element.add(element)

    result = spiderweb_custom_max_element.size()
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
        spiderweb_custom_max_element: SpiderWeb,
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
        spiderweb_custom_max_element.add(i)

    if expected_index == ValueError:
        with pytest.raises(ValueError):
            spiderweb_custom_max_element.get_maximum_index_for_level(level)
    else:
        result = spiderweb_custom_max_element.get_maximum_index_for_level(level)
        assert_that(result).is_equal_to(expected_index)


@pytest.mark.spider_web
def test_print_empty_spiderweb(capsys, spiderweb_default_max_element: SpiderWeb) -> None:
    """
    Test the print method for an empty SpiderWeb.
    """
    spiderweb_default_max_element.print()
    captured = capsys.readouterr()
    assert_that(captured.out).is_empty()


@pytest.mark.spider_web
def test_print_non_empty_spiderweb(capsys, spiderweb_custom_max_element: SpiderWeb) -> None:
    """
    Test the print method for a non-empty SpiderWeb.
    """
    for i in range(7):
        spiderweb_custom_max_element.add(i)

    spiderweb_custom_max_element.print()
    captured = capsys.readouterr()

    expected_output = ("value: 0, level: 0, index: 0\n"
                       "value: 1, level: 0, index: 1\n"
                       "value: 2, level: 0, index: 2\n"
                       "value: 3, level: 1, index: 0\n"
                       "value: 4, level: 1, index: 1\n"
                       "value: 5, level: 1, index: 2\n"
                       "value: 6, level: 2, index: 0\n")
    assert_that(captured.out).is_equal_to(expected_output)


@pytest.mark.spider_web
def test_add_element_to_empty_spiderweb(spiderweb_default_max_element: SpiderWeb) -> None:
    """
    Test adding an element to an empty SpiderWeb.
    """
    spiderweb_default_max_element.add("value")

    assert_common_properties_add(spiderweb_default_max_element, ["value"])
    (assert_that(spiderweb_default_max_element.get_first_node()).
     is_equal_to(spiderweb_default_max_element.get_last_node()))


@pytest.mark.spider_web
def test_add_element_to_non_empty_spiderweb(spiderweb_default_max_element: SpiderWeb) -> None:
    """
    Test adding an element to a non-empty SpiderWeb.
    """
    values = ["value1", "value2"]
    for value in values:
        spiderweb_default_max_element.add(value)

    assert_common_properties_add(spiderweb_default_max_element, values, index=1, level=0)
    (assert_that(spiderweb_default_max_element.get_first_node()).
     is_not_equal_to(spiderweb_default_max_element.get_last_node()))
    (assert_that(spiderweb_default_max_element.get_first_node().get_next_node()).
     is_equal_to(spiderweb_default_max_element.get_last_node()))
    (assert_that(spiderweb_default_max_element.get_last_node().get_prev_node()).
     is_equal_to(spiderweb_default_max_element.get_first_node()))


@pytest.mark.spider_web
def test_add_node_to_empty_spiderweb(spiderweb_default_max_element: SpiderWeb) -> None:
    """
    Test adding a SpiderWebNode to an empty SpiderWeb.
    """

    node = SpiderWebNode("value")
    spiderweb_default_max_element.add(node)

    assert_common_properties_add_node(spiderweb_default_max_element, [node])
    (assert_that(spiderweb_default_max_element.get_first_node()).
     is_equal_to(spiderweb_default_max_element.get_last_node()))


@pytest.mark.spider_web
def test_add_node_to_non_empty_spiderweb(spiderweb_default_max_element: SpiderWeb) -> None:
    """
    Test adding a SpiderWebNode to a non-empty SpiderWeb.
    """
    nodes = [SpiderWebNode("value1"), SpiderWebNode("value2")]
    for node in nodes:
        spiderweb_default_max_element.add(node)

    assert_common_properties_add_node(spiderweb_default_max_element, nodes, index=1, level=0)
    (assert_that(spiderweb_default_max_element.get_first_node()).
     is_not_equal_to(spiderweb_default_max_element.get_last_node()))
    (assert_that(spiderweb_default_max_element.get_first_node().get_next_node()).
     is_equal_to(spiderweb_default_max_element.get_last_node()))
    (assert_that(spiderweb_default_max_element.get_last_node().get_prev_node()).
     is_equal_to(spiderweb_default_max_element.get_first_node()))


@pytest.mark.spider_web
def test_add_first_element_to_empty_spiderweb(spiderweb_default_max_element: SpiderWeb) -> None:
    """
    Test adding an element to the beginning of an empty SpiderWeb.
    """
    spiderweb_default_max_element.add_first("value")

    assert_common_properties_add(spiderweb_default_max_element, ["value"])
    (assert_that(spiderweb_default_max_element.get_first_node()).
     is_equal_to(spiderweb_default_max_element.get_last_node()))


@pytest.mark.spider_web
def test_add_first_element_to_non_empty_spiderweb(spiderweb_default_max_element: SpiderWeb) -> None:
    """
    Test adding an element to the beginning of a non-empty SpiderWeb.
    """
    values = ["value1", "value2"]
    for value in values:
        spiderweb_default_max_element.add_first(value)
    values.reverse()

    assert_common_properties_add(spiderweb_default_max_element, values, index=1, level=0)

    (assert_that(spiderweb_default_max_element.get_first_node()).
     is_not_equal_to(spiderweb_default_max_element.get_last_node()))
    (assert_that(spiderweb_default_max_element.get_first_node().get_next_node()).
     is_equal_to(spiderweb_default_max_element.get_last_node()))
    (assert_that(spiderweb_default_max_element.get_last_node().get_prev_node()).
     is_equal_to(spiderweb_default_max_element.get_first_node()))


@pytest.mark.spider_web
def test_add_first_node_to_empty_spiderweb(spiderweb_default_max_element: SpiderWeb) -> None:
    """
    Test adding a SpiderWebNode to the beginning of an empty SpiderWeb.
    """
    node = SpiderWebNode("value")
    spiderweb_default_max_element.add_first(node)

    assert_common_properties_add_node(spiderweb_default_max_element, [node])
    (assert_that(spiderweb_default_max_element.get_first_node()).
     is_equal_to(spiderweb_default_max_element.get_last_node()))


@pytest.mark.spider_web
def test_add_first_node_to_non_empty_spiderweb(spiderweb_default_max_element: SpiderWeb) -> None:
    """
    Test adding a SpiderWebNode to the beginning of a non-empty SpiderWeb.
    """
    nodes = [SpiderWebNode("value1"), SpiderWebNode("value2")]
    for node in nodes:
        spiderweb_default_max_element.add_first(node)
    nodes.reverse()

    assert_common_properties_add_node(spiderweb_default_max_element, nodes, index=1, level=0)
    (assert_that(spiderweb_default_max_element.get_first_node()).
     is_not_equal_to(spiderweb_default_max_element.get_last_node()))
    (assert_that(spiderweb_default_max_element.get_first_node().get_next_node()).
     is_equal_to(spiderweb_default_max_element.get_last_node()))
    (assert_that(spiderweb_default_max_element.get_last_node().get_prev_node()).
     is_equal_to(spiderweb_default_max_element.get_first_node()))


@pytest.mark.spider_web
def test_add_last_element_to_empty_spiderweb(spiderweb_default_max_element: SpiderWeb) -> None:
    """
    Test adding an element to the end of an empty SpiderWeb.
    """
    spiderweb_default_max_element.add_last("value")

    assert_common_properties_add(spiderweb_default_max_element, ["value"])
    (assert_that(spiderweb_default_max_element.get_first_node()).
     is_equal_to(spiderweb_default_max_element.get_last_node()))


@pytest.mark.spider_web
def test_add_last_element_to_non_empty_spiderweb(spiderweb_default_max_element: SpiderWeb) -> None:
    """
    Test adding an element to the end of a non-empty SpiderWeb.
    """
    values = ["value1", "value2"]
    for value in values:
        spiderweb_default_max_element.add(value)

    assert_common_properties_add(spiderweb_default_max_element, values, index=1, level=0)
    (assert_that(spiderweb_default_max_element.get_first_node()).
     is_not_equal_to(spiderweb_default_max_element.get_last_node()))
    (assert_that(spiderweb_default_max_element.get_first_node().get_next_node()).
     is_equal_to(spiderweb_default_max_element.get_last_node()))
    (assert_that(spiderweb_default_max_element.get_last_node().get_prev_node()).
     is_equal_to(spiderweb_default_max_element.get_first_node()))


@pytest.mark.spider_web
def test_add_last_node_to_empty_spiderweb(spiderweb_default_max_element: SpiderWeb) -> None:
    """
    Test adding a SpiderWebNode to the end of an empty SpiderWeb.
    """
    node = SpiderWebNode("value")
    spiderweb_default_max_element.add(node)

    assert_common_properties_add_node(spiderweb_default_max_element, [node])
    (assert_that(spiderweb_default_max_element.get_first_node()).
     is_equal_to(spiderweb_default_max_element.get_last_node()))


@pytest.mark.spider_web
def test_add_last_node_to_non_empty_spiderweb(spiderweb_default_max_element: SpiderWeb) -> None:
    """
    Test adding a SpiderWebNode to the end of a non-empty SpiderWeb.
    """
    nodes = [SpiderWebNode("value1"), SpiderWebNode("value2")]
    for node in nodes:
        spiderweb_default_max_element.add(node)

    assert_common_properties_add_node(spiderweb_default_max_element, nodes, index=1, level=0)
    (assert_that(spiderweb_default_max_element.get_first_node()).
     is_not_equal_to(spiderweb_default_max_element.get_last_node()))
    (assert_that(spiderweb_default_max_element.get_first_node().get_next_node()).
     is_equal_to(spiderweb_default_max_element.get_last_node()))
    (assert_that(spiderweb_default_max_element.get_last_node().get_prev_node()).
     is_equal_to(spiderweb_default_max_element.get_first_node()))


@pytest.mark.parametrize("value, expected_level, expected_index", [
    (0, 0, 0),
    (1, 0, 1),
    (4, 1, 1)
])
@pytest.mark.spider_web
def test_index_of_element_in_spiderweb(
        spiderweb_with_values: SpiderWeb,
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
    result = spiderweb_with_values.index_of(value)
    assert_that(result).is_equal_to({"level": expected_level, "index": expected_index})


@pytest.mark.spider_web
def test_index_of_node_in_spiderweb(spiderweb_with_nodes: Tuple[SpiderWeb, List[SpiderWebNode]]) -> None:
    """
    Test the index_of method for finding a node in the SpiderWeb.
    """
    spiderweb, nodes = spiderweb_with_nodes
    result = spiderweb.index_of(node=nodes[1])
    assert_that(result).is_equal_to({"level": 0, "index": 1})


@pytest.mark.spider_web
def test_index_of_element_not_in_spiderweb(spiderweb_with_values: SpiderWeb) -> None:
    """
    Test the index_of method when the element is not present in the SpiderWeb.
    """
    result = spiderweb_with_values.index_of(10)
    assert_that(result).is_equal_to({"level": None, "index": None})


@pytest.mark.spider_web
def test_index_of_node_not_in_spiderweb(spiderweb_with_nodes: Tuple[SpiderWeb, List[SpiderWebNode]]) -> None:
    """
    Test the index_of method when the node is not present in the SpiderWeb.
    """
    spiderweb, nodes = spiderweb_with_nodes
    new_node = SpiderWebNode(10)
    result = spiderweb.index_of(node=new_node)
    assert_that(result).is_equal_to({"level": None, "index": None})


@pytest.mark.parametrize("value, expected_level, expected_index", [
    (0, 0, 0),
    (1, 1, 2),
    (3, 2, 1),
    (4, 1, 1)
])
@pytest.mark.spider_web
def test_last_index_of_element_in_spiderweb(
        spiderweb_with_values: SpiderWeb,
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
    result = spiderweb_with_values.last_index_of(value)
    assert_that(result).is_equal_to({"level": expected_level, "index": expected_index})


@pytest.mark.spider_web
def test_last_index_of_node_in_spiderweb(spiderweb_with_nodes: Tuple[SpiderWeb, List[SpiderWebNode]]) -> None:
    """
    Test the last_index_of method for finding the last occurrence of a node in the SpiderWeb.
    """
    spiderweb, nodes = spiderweb_with_nodes
    result = spiderweb.last_index_of(node=nodes[1])
    assert_that(result).is_equal_to({"level": 0, "index": 1})


@pytest.mark.spider_web
def test_last_index_of_element_not_in_spiderweb(spiderweb_with_values: SpiderWeb) -> None:
    """
    Test the last_index_of method when the element is not present in the SpiderWeb.
    """
    result = spiderweb_with_values.last_index_of(10)
    assert_that(result).is_equal_to({"level": None, "index": None})


@pytest.mark.spider_web
def test_last_index_of_node_not_in_spiderweb(spiderweb_with_nodes: Tuple[SpiderWeb, List[SpiderWebNode]]) -> None:
    """
    Test the last_index_of method when the node is not present in the SpiderWeb.
    """
    spiderweb, nodes = spiderweb_with_nodes
    new_node = SpiderWebNode(10)
    result = spiderweb.last_index_of(node=new_node)
    assert_that(result).is_equal_to({"level": None, "index": None})

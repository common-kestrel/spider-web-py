import pytest
from assertpy import assert_that
from spider_web import SpiderWebNode


@pytest.fixture(scope="function")
def spider_web_node() -> SpiderWebNode:
    # Fixture to create a SpiderWebNode for testing

    return SpiderWebNode(value="test_value")


@pytest.mark.spider_web_node
def test_get_value(spider_web_node: SpiderWebNode) -> None:
    """
    Test if the get_value method returns the correct initial value set during initialization.
    """
    result = spider_web_node.get_value()
    assert_that(result).is_equal_to("test_value")


@pytest.mark.spider_web_node
def test_get_value_returns_none_if_value_is_none() -> None:
    """
    Test if the get_value method returns None when the value is explicitly set to None.
    """
    spider_web_node = SpiderWebNode(value=None)
    result = spider_web_node.get_value()
    assert_that(result).is_none()


@pytest.mark.spider_web_node
def test_set_value_updates_value(spider_web_node: SpiderWebNode) -> None:
    """
    Test if the set_value method correctly updates the value of the node.
    """
    assert_that(spider_web_node.get_value()).is_equal_to('test_value')
    spider_web_node.set_value('updated_value')
    result = spider_web_node.get_value()
    assert_that(result).is_equal_to('updated_value')


@pytest.mark.spider_web_node
def test_set_value_can_set_value_to_none(spider_web_node: SpiderWebNode) -> None:
    """
    Test if the set_value method can set the value of the node to None.
    """
    assert_that(spider_web_node.get_value()).is_equal_to('test_value')
    spider_web_node.set_value(None)
    result = spider_web_node.get_value()
    assert_that(result).is_none()


@pytest.mark.spider_web_node
def test_set_value_can_set_value_to_numeric_value(spider_web_node: SpiderWebNode) -> None:
    """
    Test if the set_value method can set the value of the node to a numeric value.
    """
    assert_that(spider_web_node.get_value()).is_equal_to('test_value')
    spider_web_node.set_value(42)
    result = spider_web_node.get_value()
    assert_that(result).is_equal_to(42)


@pytest.mark.spider_web_node
def test_get_next_node_returns_none_when_not_set(spider_web_node: SpiderWebNode) -> None:
    """
    Test if the get_next_node method returns None when the next node is not set.
    """
    result = spider_web_node.get_next_node()
    assert_that(result).is_none()


@pytest.mark.spider_web_node
def test_get_next_node_returns_correct_next_node(spider_web_node: SpiderWebNode) -> None:
    """
    Test if the get_next_node method returns the correct next node when it is set.
    """
    next_node = SpiderWebNode(value='next_node_value')
    spider_web_node.set_next_node(next_node)
    result = spider_web_node.get_next_node()
    assert_that(result).is_equal_to(next_node)


@pytest.mark.spider_web_node
def test_set_next_node_updates_node(spider_web_node: SpiderWebNode) -> None:
    """
    Test if the set_next_node method correctly updates the next node.
    """
    next_node = SpiderWebNode(value=42)
    spider_web_node.set_next_node(next_node)
    result = spider_web_node.get_next_node()
    assert_that(result).is_equal_to(next_node)

    next_node = SpiderWebNode(value="updated_node")
    spider_web_node.set_next_node(next_node)
    result = spider_web_node.get_next_node()
    assert_that(result).is_equal_to(next_node)
    assert_that(result.get_next_node()).is_none()


@pytest.mark.spider_web_node
def test_set_next_node_can_set_next_node_to_none(spider_web_node: SpiderWebNode) -> None:
    """
    Test if the set_next_node method can set the next node to None.
    """
    next_node = SpiderWebNode(value=42)
    spider_web_node.set_next_node(next_node)
    result = spider_web_node.get_next_node()
    assert_that(result).is_equal_to(next_node)

    spider_web_node.set_next_node(next_node=None)
    result = spider_web_node.get_next_node()
    assert_that(result).is_none()

import pytest
from assertpy import assert_that
from spider_web import SpiderWeb, SpiderWebNode


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

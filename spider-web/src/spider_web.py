from typing import Optional, Any


class SpiderWebNode:
    """
    The `SpiderWebNode` class represents a node in the SpiderWeb data structure, where each node
    stores a value and maintains references to its next and previous nodes, as well
    as references to nodes on the next and previous levels.

    Example Usage:
        >>> node = SpiderWebNode(53, None, None)

    Attributes:
        - `value`: The value stored in the node.
        - `prev_node`: Reference to the previous node.
        - `prev_level_node`: Reference to the node on the previous level.
    """

    def __init__(
            self,
            value: Any,
            prev_node: Optional['SpiderWebNode'] = None,
            prev_level_node: Optional['SpiderWebNode'] = None
    ):
        """
            Initialize a SpiderWebNode.

            :param value: The value to be stored in the node.
            :type value: Any
            :param prev_node: Reference to the previous node.
            :type prev_node: :class:`SpiderWebNode` or None, optional
            :param prev_level_node: Reference to the node on the previous level.
            :type prev_level_node: :class:`SpiderWebNode` or None, optional
        """
        self._value = value
        self._prev_node = prev_node
        self._prev_level_node = prev_level_node
        self._next_node = None
        self._next_level_node = None

    def get_value(self) -> Any:
        """
        Gets the value stored in the node.

        :return: The value stored in the node.
        """
        return self._value

    def set_value(self, value: Any) -> None:
        """
        Sets the value of the node.

        :param value: The new value to be stored in the node.
        """
        self._value = value

    def get_next_node(self) -> Optional['SpiderWebNode']:
        """
        Gets the reference to the next node.

        :return: The next node.
        """
        return self._next_node

    def set_next_node(self, next_node: Optional['SpiderWebNode']) -> None:
        """
        Sets the reference to the next node.

        :param next_node: The next node.
        """
        self._next_node = next_node

    def get_prev_node(self) -> Optional['SpiderWebNode']:
        """
        Gets the reference to the previous node.

        :return: The previous node.
        """
        return self._prev_node

    def set_prev_node(self, prev_node: Optional['SpiderWebNode']) -> None:
        """
        Sets the reference to the previous node.

        :param prev_node: The previous node.
        """
        self._prev_node = prev_node

    def get_next_level_node(self) -> Optional['SpiderWebNode']:
        """
        Gets the reference to the node on the next level.

        :return: The node on the next level.
        """
        return self._next_level_node

    def set_next_level_node(self, next_level_node: Optional['SpiderWebNode']) -> None:
        """
        Sets the reference to the node on the next level.

        :param next_level_node: The node on the next level.
        """
        self._next_level_node = next_level_node

    def get_prev_level_node(self) -> Optional['SpiderWebNode']:
        """
        Gets the reference to the node on the previous level.

        :return: The node on the previous level.
        """
        return self._prev_level_node

    def set_prev_level_node(self, prev_level_node: Optional['SpiderWebNode']) -> None:
        """
        Sets the reference to the node on the previous level.

        :param prev_level_node: The node on the previous level.
        """
        self._prev_level_node = prev_level_node

    def reset_pointers(self) -> None:
        """
        Resets the pointers of the SpiderWebNode, setting all references to None.
        """
        self._prev_node = None
        self._next_node = None
        self._prev_level_node = None
        self._next_level_node = None

    def __str__(self):
        """
            Return a string representation of the SpiderWebNode.

            Example:
                >>> node = SpiderWebNode(53, None, None)
                >>> print(node)
                'SpiderWebNode(value=53, prev_node=None, prev_level_node=None, next_node=None, next_level_node=None)'

            :return: A string representation of the SpiderWebNode.
            :rtype: str
        """
        return (
            f"SpiderWebNode("
            f"value={self._value}, "
            f"prev_node={self._prev_node}, "
            f"prev_level_node={self._prev_level_node}, "
            f"next_node={self._next_node}, "
            f"next_level_node={self._next_level_node}"
            f")"
        )


class SpiderWeb:
    """
        SpiderWeb is a custom data structure designed to organize elements in a hierarchical
        and indexed manner. It is implemented as a linked structure with nodes organized in
        levels and indices. The class provides methods for adding, querying, and removing
        elements based on their levels and indices within the SpiderWeb.


        Example Usage:
            >>> spider_web = SpiderWeb()
            >>> spider_web.add(1)
            >>> spider_web.add(2)
            >>> spider_web.add(3)
            >>> spider_web.print()

        Attributes:
            - `max_element_per_level`: The maximum number of elements allowed per level (6).

        """
    def __init__(self, max_element_per_level: int = 6):
        self._value: Any = None
        self._first: Optional[SpiderWebNode] = None
        self._prev_level: Optional[SpiderWebNode] = None
        self._last: Optional[SpiderWebNode] = None
        self._level: int = 0
        self._index: int = 0
        self._tmp_level: int = 0
        self._tmp_index: int = 0
        self._size: int = 0
        self._max_element_per_level = max_element_per_level

    # Getter methods for accessing SpiderWeb properties

    def get_first_node(self) -> Optional[SpiderWebNode]:
        """
        Gets the first node in the SpiderWeb.

        :return: The first node in the SpiderWeb.
        :rtype: Optional[SpiderWebNode]
        """
        return self._first

    def get_prev_level(self) -> Optional[SpiderWebNode]:
        """
        Gets the previous level node in the SpiderWeb.

        :return: The previous level pointer in the SpiderWeb.
        :rtype: Optional[SpiderWebNode]
        """
        return self._prev_level

    def get_last_node(self) -> Optional[SpiderWebNode]:
        """
        Gets the last node in the SpiderWeb.

        :return: The last node in the SpiderWeb.
        :rtype: Optional[SpiderWebNode]
        """
        return self._last

    def get_level(self) -> int:
        """
        Gets the last level of the SpiderWeb.

        :return: The last level of the SpiderWeb.
        :rtype: int
        """
        if self._first is None:
            return -1
        if self._index == 0:
            return self._level - 1
        return self._level

    def get_index(self) -> int:
        """
        Gets the last index of the SpiderWeb.

        :return: The last index of the SpiderWeb.
        :rtype: int
        """
        if self._first is None:
            return -1
        if self._index == 0:
            return self._max_element_per_level - 1
        return self._index - 1

    # Private helper methods for internal operations and data management within the SpiderWebNode class.

    def _reset_pointers(self) -> None:
        self._first = None
        self._last = None
        self._prev_level = None

    def _reset_spider_web(self) -> None:
        self._reset_pointers()
        self._level = 0
        self._index = 0
        self._size = 0

    def _reset_tmp_variables(self) -> None:
        self._tmp_level = 0
        self._tmp_index = 0

    def _reset_tmp_variables_last(self) -> None:
        self._tmp_index = self._index - 1
        if self._tmp_index < 0:
            self._tmp_index = self._max_element_per_level - 1
            self._tmp_level = self._level - 1
        else:
            self._tmp_level = self._level

    def _next_index(self) -> None:
        self._tmp_index += 1
        if self._tmp_index == self._max_element_per_level:
            self._tmp_level += 1
            self._tmp_index = 0

    def _prev_index(self) -> None:
        self._tmp_index -= 1
        if self._tmp_index == -1:
            self._tmp_level -= 1
            self._tmp_index = self._max_element_per_level - 1

    def _increment_index(self) -> None:
        self._index += 1
        if self._index == self._max_element_per_level:
            if self._level == 0:
                self._prev_level = self._first
            self._level += 1
            self._index = 0

    def _decrement_index(self) -> None:
        if self._index > 0:
            self._index -= 1
        else:
            self._index = self._max_element_per_level - 1
            self._level -= 1

    def _increment_size(self) -> None:
        self._size += 1

    def _decrement_size(self) -> None:
        self._size -= 1

    def _is_valid_level_and_index(self, level: int, index: int) -> bool:
        return (0 <= level <= self.get_level()) and (0 <= index <= self.get_maximum_index_for_level(level))

    def _add_first_node(self, new_node: Optional[SpiderWebNode]) -> None:
        if self._first is None:
            self._first = new_node
            self._last = new_node
        else:
            self._first.set_prev_node(new_node)
            new_node.set_next_node(self._first)
            self._first = new_node

            if self._size >= self._max_element_per_level:
                tmp_pointer = self._first
                for i in range(self._max_element_per_level):
                    tmp_pointer = tmp_pointer.get_next_node()

                self._first.set_next_level_node(tmp_pointer)
                tmp_pointer.set_prev_level_node(self._first)

        self._increment_index()
        self._increment_size()

    def _add_last_node(self, new_node: Optional[SpiderWebNode]) -> None:
        if self._first is None:
            self._first = new_node
            self._last = new_node
        else:
            self._last.set_next_node(new_node)
            self._last = new_node
            if self._prev_level is not None:
                self._prev_level.set_next_level_node(new_node)
                self._prev_level = self._prev_level.get_next_node()

        self._increment_index()
        self._increment_size()

    # Other public methods...

    def get_maximum_index_for_level(self, level: int) -> int:
        """
        Gets the maximum index for a specified level in the SpiderWeb.

        :param level: The level for which to retrieve the maximum index.
        :type level: int
        :return: The maximum index for the specified level.
        :rtype: int
        :raises ValueError: If the specified level is negative or exceeds the maximum level in the SpiderWeb.
        :raises ValueError: If the SpiderWeb is empty, and the maximum index cannot be determined.
        """
        if level < 0:
            raise ValueError("Invalid level: Level cannot be negative.")
        if self._first is None:
            raise ValueError("Cannot get maximum index for level on an empty SpiderWeb")
        if level > self.get_level():
            raise ValueError(f"Invalid level: {level} exceeds the maximum level {self.get_level()}.")

        if level < self.get_level():
            return self._max_element_per_level - 1

        return self.get_index()

    def add(self, value: Any) -> None:
        """
        Adds the specified element to the end of the SpiderWeb.

        :param value: The value to be added to the end of the SpiderWeb.
        :type value: Any
        :return: None
        """
        new_node = SpiderWebNode(value, self._last, self._prev_level)
        self._add_last_node(new_node)

    def print(self) -> None:
        """
        Prints the elements of the SpiderWeb along with their levels and indices.
        This method prints the elements stored in the SpiderWeb, displaying their levels
        and indices within the structure.

        :return: None
        """
        current: Optional[SpiderWebNode] = self._first
        self._reset_tmp_variables()
        while current is not None:
            print(f"value: {current.get_value()}, level: {self._tmp_level}, index: {self._tmp_index}")
            current = current.get_next_node()
            self._next_index()

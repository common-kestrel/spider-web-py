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

    def get_value(self):
        """
        Gets the value stored in the node.

        :return: The value stored in the node.
        """
        return self._value

    def set_value(self, value):
        """
        Sets the value of the node.

        :param value: The new value to be stored in the node.
        """
        self._value = value

    def get_next_node(self):
        """
        Gets the reference to the next node.

        :return: The next node.
        """
        return self._next_node

    def set_next_node(self, next_node):
        """
        Sets the reference to the next node.

        :param next_node: The next node.
        """
        self._next_node = next_node

    def get_prev_node(self):
        """
        Gets the reference to the previous node.

        :return: The previous node.
        """
        return self._prev_node

    def set_prev_node(self, prev_node):
        """
        Sets the reference to the previous node.

        :param prev_node: The previous node.
        """
        self._prev_node = prev_node

    def get_next_level_node(self):
        """
        Gets the reference to the node on the next level.

        :return: The node on the next level.
        """
        return self._next_level_node

    def set_next_level_node(self, next_level_node):
        """
        Sets the reference to the node on the next level.

        :param next_level_node: The node on the next level.
        """
        self._next_level_node = next_level_node

    def get_prev_level_node(self):
        """
        Gets the reference to the node on the previous level.

        :return: The node on the previous level.
        """
        return self._prev_level_node

    def set_prev_level_node(self, prev_level_node):
        """
        Sets the reference to the node on the previous level.

        :param prev_level_node: The node on the previous level.
        """
        self._prev_level_node = prev_level_node

    def reset_pointers(self):
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

    def _reset_tmp_variables(self):
        self._tmp_level = 0
        self._tmp_index = 0

    def _next_index(self):
        self._tmp_index += 1
        if self._tmp_index == self._max_element_per_level:
            self._tmp_level += 1
            self._tmp_index = 0

    def _increment_index(self):
        self._index += 1
        if self._index == self._max_element_per_level:
            if self._level == 0:
                self._prev_level = self._first
            self._level += 1
            self._index = 0

    def _increment_size(self):
        self._size += 1

    def _add_last_node(self, new_node: Optional[SpiderWebNode]):
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

    def add(self, value: Any):
        new_node = SpiderWebNode(value, self._last, self._prev_level)
        self._add_last_node(new_node)

    def print(self):
        current: Optional['SpiderWebNode'] = self._first
        self._reset_tmp_variables()
        while current is not None:
            print(f"value: {current.get_value()}, level: {self._tmp_level}, index: {self._tmp_index}")
            current = current.get_next_node()
            self._next_index()

from typing import Optional, Any


class SpiderWebNode:
    """
    The `SpiderWebNode` class represents a node in the SpiderWeb data structure, where each node
    stores a value and maintains references to its next and previous nodes, as well
    as references to nodes on the next and previous levels.

    Example Usage:
        >>> node = SpiderWebNode(42, None, None)

    Attributes:
        - `value`: The value stored in the node.
        - `prev_node`: Reference to the previous node.
        - `prev_level_node`: Reference to the node on the previous level.
    """

    def __init__(
            self, value: Any,
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
        self.value = value
        self.prev_node = prev_node
        self.prev_level_node = prev_level_node
        self.next_node = None
        self.next_level_node = None

    def get_value(self):
        """
        Gets the value stored in the node.

        :return: The value stored in the node.
        """
        return self.value

    def set_value(self, value):
        """
        Sets the value of the node.

        :param value: The new value to be stored in the node.
        """
        self.value = value

    def get_next_node(self):
        """
        Gets the reference to the next node.

        :return: The next node.
        """
        return self.next_node

    def set_next_node(self, next_node):
        """
        Sets the reference to the next node.

        :param next_node: The next node.
        """
        self.next_node = next_node

    def get_prev_node(self):
        """
        Gets the reference to the previous node.

        :return: The previous node.
        """
        return self.prev_node

    def set_prev_node(self, prev_node):
        """
        Sets the reference to the previous node.

        :param prev_node: The previous node.
        """
        self.prev_node = prev_node

    def get_next_level_node(self):
        """
        Gets the reference to the node on the next level.

        :return: The node on the next level.
        """
        return self.next_level_node

    def set_next_level_node(self, next_level_node):
        """
        Sets the reference to the node on the next level.

        :param next_level_node: The node on the next level.
        """
        self.next_level_node = next_level_node

    def get_prev_level_node(self):
        """
        Gets the reference to the node on the previous level.

        :return: The node on the previous level.
        """
        return self.prev_level_node

    def set_prev_level_node(self, prev_level_node):
        """
        Sets the reference to the node on the previous level.

        :param prev_level_node: The node on the previous level.
        """
        self.prev_level_node = prev_level_node

    def reset_pointers(self):
        """
        Resets the pointers of the SpiderWebNode, setting all references to None.
        """
        self.prev_node = None
        self.next_node = None
        self.prev_level_node = None
        self.next_level_node = None

    def __str__(self):
        """
            Return a string representation of the SpiderWebNode.

            Example:
                >>> node = SpiderWebNode(42, None, None)
                >>> print(node)
                'SpiderWebNode(value=53, prev_node=None, prev_level_node=None, next_node=None, next_level_node=None)'

            :return: A string representation of the SpiderWebNode.
            :rtype: str
        """
        return (
            f"SpiderWebNode("
            f"value={self.value}, "
            f"prev_node={self.prev_node}, "
            f"prev_level_node={self.prev_level_node}, "
            f"next_node={self.next_node}, "
            f"next_level_node={self.next_level_node}"
            f")"
        )

class SpiderWebNode:
    """
    The `SpiderWebNode` class represents a node in the SpiderWeb data structure, where each node
    stores a value and maintains references to its next and previous nodes, as well
    as references to nodes on the next and previous levels.

    Example Usage:
    >>> node = SpiderWebNode(42, None, None)
    """

    def __init__(self, value, prev_node, prev_level_node):
        """
        Constructs a SpiderWebNode with the specified value, previous node, and previous level node.

        :param value: The value to be stored in the node.
        :type value: Any
        :param prev_node: Reference to the previous node.
        :type prev_node: SpiderWebNode or None
        :param prev_level_node: Reference to the node on the previous level.
        :type prev_level_node: SpiderWebNode or None
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
        Returns a string representation of the SpiderWebNode.

        :return: A string representation of the SpiderWebNode, including its value.
        """
        return f"SpiderWebNode{{value={self.value}}}"

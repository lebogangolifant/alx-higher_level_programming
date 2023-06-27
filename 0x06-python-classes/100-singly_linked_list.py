#!/usr/bin/python3
"""
Class Node that defines a node of a singly linked list by:
"""


class Node:
    """Represents a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a node.

        Args:
            data (int): The data value of the node.
            next_node (Node): Next node in the linked list. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data value of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data value of the node.

        Args:
            value (int): The data value to set.

        Raises:
            TypeError: If data is not an integer.
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node in the linked list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node in the linked list.

        Args:
            value (Node): The next node to set.

        Raises:
            TypeError: If next_node is not a Node object or None.
        """
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        """Initializes an empty singly linked list."""
        self.head = None

    def sorted_insert(self, value):
        """Insert new Node into the correct sorted position (increasing order).

        Args:
            value (int): The value of the new Node to be inserted.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and \
                    value > current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Returns a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)

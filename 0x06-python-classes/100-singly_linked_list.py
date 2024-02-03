#!/usr/bin/python3
"""Singly LL implementation"""


class Node:
    """Node
    class Node that defines a node of a singly linked list by
    """

    def __init__(self, data, next_node=None):
        """Constructor"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Data reper"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """return the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter for node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """SinglyLinkedList"""

    def __init__(self):
        """construct the list"""
        self.__head = None

    def sorted_insert(self, value):
        """inset Node"""
        node = Node(value)
        if not self.__head:
            self.__head = node
        else:
            if self.__head and self.__head.data > value:
                node.next_node = self.__head
                self.__head = node
            else:
                tmp = self.__head
                prev = tmp
                while tmp and tmp.data < value:
                    prev = tmp
                    tmp = tmp.next_node
                node.next_node = tmp
                prev.next_node = node

    def __str__(self):
        """print the lisr"""
        tmp = self.__head
        res = ""
        i = 0
        while tmp:
            res += ("" if not i else "\n") + str(tmp.data)
            tmp = tmp.next_node
            if not i:
                i = 1
        return res

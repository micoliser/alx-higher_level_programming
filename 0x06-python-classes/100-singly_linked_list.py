#!/usr/bin/python3
""" This module contains a sinngly linked list class and a node class.
    The node class has private instance attributes data and next node.
    The list class has private instance attribute head with
    no setter and getter property. """


class Node:
    """ A node class which is the node of a singly linked list """

    def __init__(self, data, next_node=None):
        """ Initialize self """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ Returns the node data """
        return self.__data

    @data.setter
    def data(self, value):
        """ Sets the data to value """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Returns the next node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Sets the next node to value """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ A singly linked list class with nodes """

    def __init__(self):
        """ Initializes self """
        self.__head = []

    def __str__(self):
        """ Printing self """
        s = ""
        i = 0
        for node in self.__head:
            s += str(node.data)
            if i != len(self.__head) - 1:
                s += "\n"
            i += 1
        return s

    def sorted_insert(self, value):
        """ Insert a new Node into the correct sorted position in the list
        (increasing order) """
        new = Node(value)
        if len(self.__head) == 0:
            self.__head.append(new)
        else:
            i = 0
            done = False
            for node in self.__head:
                if node.data >= value:
                    self.__head[i - 1].next_node = new
                    new.next_node = node
                    self.__head = self.__head[:i] + [new] + self.__head[i:]
                    done = True
                    break
                i += 1
            if not done:
                self.__head[-1].next_node = new
                self.__head.append(new)

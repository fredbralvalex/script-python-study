from linkedlist import LinkedList, Node

def print_linked_list(linked_list):
    node = linked_list.head()
    while node:
        print(node.value)
        node = node.next

import unittest

class LinkedListTests(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList

    def test_reversed_list(self):
        self.linked_list.insert_node_to_tail(Node('1'))
        self.linked_list.insert_node_to_tail(Node('2'))
        self.linked_list.insert_node_to_tail(Node('3'))
        self.linked_list.insert_node_to_tail(Node('4'))
        self.linked_list.insert_node_to_tail(Node('5'))
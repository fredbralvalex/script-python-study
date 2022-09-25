class Node:
    def __init__(self, value):
        self.next = None
        self.value = value
            

class LinkedList:
    def __init__(self):
        self._head = Node(None)
    
    def insert_node_to_tail(self, node):
        tail = self.tail()
        if tail.value:
            tail.next = node
        else:
            self._head = node

    def insert_node_to_head(self, node):
        next = self._head.next
        self._head = node
        node.next = next

    def is_empty(self):
        return self._head.value == None and self._head.next == None

    def head(self):
        return self._head

    def tail(self):
        current = self._head
        while current.next:
            current = current.next
        return current

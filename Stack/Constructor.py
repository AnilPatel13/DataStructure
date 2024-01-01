class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

new_stack = Stack(4)
print("value of stack", new_stack.top.value)
print("height of stack", new_stack.height)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.fisrt = new_node
        self.last = new_node
        self.length = 1


my_queue = Queue(4)
print(my_queue.fisrt.value)
print(my_queue.last.value)
print(my_queue.length)
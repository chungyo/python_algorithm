class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

        return

    def dequeue(self):
        if self.is_empty():
            return "큐가 비어있습니다"
        delete_head = self.head
        self.head = self.head.next
        return delete_head.data

    def peek(self):
        if self.is_empty():
            return "queue is empty"

        return self.head.data

    def is_empty(self):
        return self.head is None

# 4 - 5 - 6
# 5 - 6

queue = Queue()
queue.enqueue(4)
print(queue.peek())
queue.enqueue(5)
print(queue.peek())
queue.enqueue(6)
print(queue.peek())
queue.dequeue()

print(queue.peek())
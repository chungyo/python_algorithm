class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

# str를 이용해서 풀어보았다. 이렇게하면 더 간단할 것 같다.
def get_linked_list_sum(linked_list_1, linked_list_2):
    string_sum_1 = ''
    string_sum_2 = ''
    cur_1 = linked_list_1.head
    cur_2 = linked_list_2.head

    while cur_1 is not None:
        string_sum_1 += str(cur_1.data)
        cur_1 = cur_1.next

    while cur_2 is not None:
        string_sum_2 += str(cur_2.data)
        cur_2 = cur_2.next

    return int(string_sum_1) + int(string_sum_2)

linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))

'''6.5'''
#https://seongonion.tistory.com/78
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class NormalLinkedList:
    def __init__(self):
        self.head = None

    def outputPrint(self):
        node = self.head

        while node:
            print(node.data, end=' ')
            node = node.next

    def reverse(self):
        node = self.head
        prev = None

        while node:
            print(node.data)
            tmp = node.next
            if tmp == None:
                self.head = node

            node.next = prev
            prev = node
            node = tmp


# ---------------------------------
# 밑으로는 값을 입력 받는 내용
node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)

linked_list = NormalLinkedList()

linked_list.head = node_1
node_1.next = node_2
node_2.next = node_3

linked_list.reverse()
linked_list.outputPrint()
'''6.5'''

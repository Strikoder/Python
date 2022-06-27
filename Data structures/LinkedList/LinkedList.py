class Node:
    def __init__(self, data=None, next=None ):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head=node
        self.head=node
    def print(self):
        if self.head is None:
            print("The list is already empty dude!")
            return
        itr = self.head
        llstr=''

        while itr:
            llstr+=str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

ll=LinkedList()
ll.insert_at_beginning(5)
ll.insert_at_beginning(9)
ll.print()
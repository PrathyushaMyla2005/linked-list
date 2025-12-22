# Node class represents one node in a doubly linked list
class Node:
    def __init__(self, data):
        self.data = data      # stores the value of the node
        self.next = None      # pointer to the next node (forward link)
        self.prev = None      # pointer to the previous node (backward link)


# Doubly Linked List class
class DoubleLinkedList:
    def __init__(self):
        self.head = None      # head points to the first node of the list

    # function to traverse the list in forward direction
    def traverse_forward(self):
        a = self.head         # start traversal from the head node
        while a:              # loop until a becomes None (end of list)
            print(a.data, end="->")  # print current node's data
            a = a.next        # move to the next node
        print("None")         # indicates end of forward traversal

    # function to traverse the list in backward direction
    def traverse_backward(self):
        if self.head is None:# check if the list is empty
            print("doubly linked list is empty")
        else:
            a = self.head# move to the last 
            while a.next is not None:# traverse to the end of the list
                a = a.next# move to the next node
            while a is not None:# loop until a becomes None (start of list)
                print(a.data, end="->")  # print current node's data
                a = a.prev        # move to the previous node`
            print("None")         # indicates end of backward traversal
#insert at beginning
    def insert_at_beginning(self, data):
        ns = Node(data)  # create a new node with given data
        a = self.head  # store the current head node
        a.prev = ns  # link current head's previous to new node
        ns.next = a  # link new node's next to current head
        self.head = ns  # update head to point to the new node
#insert at end
    def insert_at_end(self,data):
        ne = Node(data) # create a new node with given data
        a = self.head # start from the head node
        while a.next is not None: # traverse to the end of the list
            a = a.next # move to the next node
        a.next = ne # link last node's next to new node
        ne.prev = a # link new node's previous to last node
#creating doubly linked list and nodes
#inserting nodes and  specifying data
    def insert_at_spec(self,data,position):
        nib = Node(data) # create a new node with given data
        a = self.head # start from the head node
        for i in range(position-1): # traverse to the specified position
            a = a.next # move to the next node
        nib.prev = a # link new node's previous to node at position-1
        nib.next = a.next # link new node's next to node at position
        a.next.prev = nib # link node at position's previous to new node
        a.next = nib # link node at position-1's next to new node
#DELETE AT BEGINNING
    def delete_at_beginning(self):
        a = self.head # store the current head node
        self.head = a.next  #head points to second node
        a.next = None # first node's next set to None
        self.head.prev = None # new head's prev set to None
#deleting nodes aat end
    def delete_at_end(self):
        a = self.head # start from the head node
        before = self.head # to keep track of the node before 'a'
        while a.next is not None: # traverse to the end of the list
            before = a # update 'before' to current node
            a = a.next # move to the next node
        before.next = None # unlink the last node
        a.prev = None # unlink the last node's previous link
    def delete_at_pos(self,position):
        a = self.head.next # start from the head node
        before = self.head # to keep track of the node before 'a'
        for i in range(1, position-1): # traverse to the specified position
            a = a.next # move to the next node
            before =  before.next # update 'before' to current node
        before.next = a.next # unlink the node at the specified position
        a.next.prev = before # update the previous link of the next node
        a.next = None # unlink the node being deleted
        a.prev = None # unlink the node being deleted


# creating an object of Doubly Linked List
dll = DoubleLinkedList()      # creates an empty doubly linked list

# creating first node
n1 = Node(5)                 # node with data 5

# creating second node
n2 = Node(10)                # node with data 10

# creating third node
n3 = Node(15)                # node with data 15
#creating fourth node
n4 = Node(20)                # node with data 20


# connecting nodes to form doubly linked list
dll.head = n1                # head points to first node

n1.next = n2                 # first node points forward to second node
n2.prev = n1                 # second node points backward to first node

n2.next = n3                 # second node points forward to third node
n3.prev = n2                 # third node points backward to second node
n3.next = n4                 # third node points forward to fourth node
n4.prev = n3                 # fourth node points backward to third node

# calling forward traversal
dll.traverse_forward()       # output: 5->10->15->None

# calling backward traversal
dll.traverse_backward()      # output: 15->10->5->None
# inserting at beginning
dll.insert_at_beginning(2)   # inserts node with data 2 at the beginning
dll.traverse_forward()       # output: 2->5->10->15->None
dll.traverse_backward()      # output: 15->10->5->2->None
# inserting at end
dll.insert_at_end(25)        # inserts node with data 25 at the end
dll.traverse_forward()       # output: 2->5->10->15->25->None
dll.traverse_backward()      # output: 25->15->10->5->2
# inserting at specific position
dll.insert_at_spec(12,2)     # inserts node with data 12 at position 2
dll.traverse_forward()       # output: 2->5->12->10->15->25->None
dll.traverse_backward()      # output: 25->15->10->12->5
dll.delete_at_beginning()    # deletes node at beginning
dll.traverse_forward()       # output: 5->12->10->15->25
dll.traverse_backward()      # output: 25->15->10->12->5
dll.delete_at_end()         # deletes node at end
dll.traverse_forward()       # output: 5->12->10->15
dll.traverse_backward()      # output: 15->10->12->5
dll.delete_at_pos(2)       # deletes node at position 2
dll.traverse_forward()       # output: 5->10->15
dll.traverse_backward()      # output: 15->10->5
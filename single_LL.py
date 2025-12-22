#creating a  node sll:
class Node:
    def __init__(self,data):#node class
        self.data = data#data part of node
        self.next = None#pointer part of node
#creating a singly linked list
class SinglyLinkedList:#singly linked list class
    def __init__(self):#initializing head to None
        self.head = None#head of the linked list
#traversing a singly linked list
    def traverse(self):
        if self.head is None:#checking if linked list is empty
            print("Linked list is empty")#printing message if empty
        else:
            a = self.head#starting from head
            while a is not None:#traversing till the end of the linked list
                print(a.data,end = "->")#printing data of each node 
                a = a.next#moving to next node
            print("None")#indicating end of linked list
    def insert_at_beginning(self,data):#inserting a node at the beginning of the singly linked list
        nb = Node(data)#new node
        nb.next = self.head#linking new node to head
        self.head = nb#updating head to new node
    def insert_at_end(self,data):#inserting a node at the end of the singly linked list
        ne = Node(data)#new node
        if self.head is None:#if linked list is empty
            self.head = next#new node becomes head
            return
        a = self.head#starting from head
        while a.next is not None:#traversing to the end of the linked list
            a = a.next#moving to next node
        a.next = ne#linking last node to new node
    def insert_at_pos(self, data, pos):#inserting a node at a specific position in the singly linked list
        npn = Node(data)#new node
        if pos == 1:#if position is 1, insert at beginning
            npn.next = self.head#linking new node to head
            self.head = npn#updating head to new node
            return#returning from function
        a = self.head#starting from head
        for i in range(1, pos-1):#traversing to the position before the desired position
         a = a.next#moving to next node
        npn.next = a.next#linking new node to the next node of current node
        a.next = npn#linking current node to new node
    def delete_at_beginning(self):#deleting a node at the beginning of the singly linked list
        a = self.head#starting from head
        self.head = a.next#updating head to next node
        a.next = None#unlinking the deleted node
    def delete_at_end(self):#deleting a node at the end of the singly linked list
        prev = self.head#starting from head
        a = self.head.next#moving to next node
        while a.next is not None:#traversing to the end of the linked list
            prev = a#updating previous node
            a = a.next#moving to next node
        prev.next = None#unlinking the last node
    def delete_at_pos(self, pos):#deleting a node at a specific position in the singly linked list
        prev = self.head#starting from head
        a = self.head.next#moving to next node
        for i in range(1, pos-1):#traversing to the position before the desired position
            prev = a#updating previous node
            a = a.next#moving to next node
        prev.next = a.next#linking previous node to the next node of current node
        a.next = None#unlinking the deleted node

#example:
n1 = Node(10)
sll = SinglyLinkedList()
sll.head = n1
n2 = Node(20)
n1.next = n2
n3 = Node(30)
n2.next = n3
sll.traverse()
sll.insert_at_beginning(5)
sll.traverse()
sll.insert_at_end(40)
sll.traverse()
sll.insert_at_pos(25,2)
sll.traverse()
sll.delete_at_beginning()
sll.traverse()
sll.delete_at_end()
sll.traverse()
sll.delete_at_pos(2)
sll.traverse()

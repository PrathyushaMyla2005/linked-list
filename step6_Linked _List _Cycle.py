'''Problem Statement
Given the head of a singly linked list, determine whether the list contains a cycle.
What is a Cycle?
A cycle exists if:
Any node’s next pointer points to a previous node Because of this, the linked list never reaches null
Input: head → head of a singly linked list
Return: True if there is a cycle in the linked list, otherwise False
Example:
head = [3 → 2 → 0 → -4]
pos = 1 (the tail connects to the second node)
Output: True
pproach Used
👉Two Pointers (Floyd’s Cycle Detection Algorithm)
Why Two Pointers?
We are not allowed to modify the list
We must use O(1) extra space
Two pointers give an optimal solution
How It Works (Explain Clearly)
Use two pointers:
Slow pointer → moves 1 step at a time
Fast pointer → moves 2 steps at a time
Start both from the head
'''
class Node:
    def __init__(self, data):#initializing a node
        self.data = data#data part of node
        self.next = None#pointer part of node
class SinglyLinkedList:#singly linked list class
    def __init__(self):
        self.head = None#head of the linked list
    def has_cycle(self, head):#function to detect cycle in linked list
        slow = head # initialize slow pointer to head
        fast = head # initialize fast pointer to head
        while fast and fast.next: # traverse the linked list
            slow = slow.next # move slow pointer by 1 step
            fast = fast.next.next # move fast pointer by 2 steps
            if slow == fast: # if both pointers meet, there is a cycle
                return True # return True
sll = SinglyLinkedList() # create a singly linked list object
sll.head = Node(3) # create head node with data 3
sll.head.next = Node(2) # create second node with data 2
sll.head.next.next = Node(0) # create third node with data 0
sll.head.next.next.next = Node(-4) # create fourth node with data -4
sll.head.next.next.next.next = sll.head.next # create a cycle by linking the
# last node to the second node
has_cycle = sll.has_cycle(sll.head) # check if the linked list has a cycle
print(has_cycle)   # OUTPUT: True
'''tc = O(n) as in the worst case, we may need to traverse the entire list.
sc = O(1) as we are using only two pointers regardless of the input size.
'''

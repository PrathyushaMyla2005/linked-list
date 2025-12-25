'''problem statement:We are given the head of a singly linked list and an integer n.
Our task is to remove the nth node from the end of the linked list and return the head of the updated list.
” What does “Nth from the end” mean? (Explain Slowly)
It means:
Start counting from the last node
The last node is 1st from the end
The node before it is 2nd from the end, and so on
Linked List: 1 → 2 → 3 → 4 → 5
n = 2
Output: 1 → 2 → 3 → 5'''
class Node:
    def __init__(self, data):#initializing a node
        self.data = data#data part of node
        self.next = None#pointer part of node
class SinglyLinkedList:#singly linked list class
    def __init__(self):#initializing head of linked list
        self.head = None
    def removeNthFromEnd(self, head, n):
        # Step 1: count total number of nodes
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        # Step 2: if head needs to be removed
        if n == length:
            return head.next

        # Step 3: move to the node before the target
        temp = head
        for _ in range(length - n - 1):
            temp = temp.next

        # Step 4: remove the nth node from end
        temp.next = temp.next.next

        return head
#example:
sll = SinglyLinkedList() # create singly linked list object
sll.head = Node(1) # create head node with data 1
sll.head.next = Node(2) # create second node with data 2
sll.head.next.next = Node(3) # create third node with data 3
sll.head.next.next.next = Node(4) # create fourth node with data 4
sll.head.next.next.next.next = Node(5) # create fifth node with data 5
n = 2 # node to be removed from end
updated_head = sll.removeNthFromEnd(sll.head, n) # remove nth node from end
# print updated linked list
temp = updated_head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
# OUTPUT: 1 -> 2 -> 3 -> 5 ->
'''tc = O(L) where L is the length of the linked list.
We traverse the list twice: once to count the nodes and once to remove the target node.
sc = O(1) as we are using only a constant amount of extra space.'''

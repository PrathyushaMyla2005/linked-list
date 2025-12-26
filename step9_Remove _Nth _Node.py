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
# using two pointer approach
class Node:#node class
    def __init__(self, data):#initializing a node
        self.data = data#data part of node
        self.next = None#pointer part of node
class SinglyLinkedList:#singly linked list class
    def __init__(self):#initializing head
        self.head = None#head of the linked list
    def remove_nth_from_end(self, head, n):#function to remove nth node from end
        dummy = Node(0) # create a dummy node
        dummy.next = head # point dummy's next to head
        first = dummy # initialize first pointer to dummy
        second = dummy # initialize second pointer to dummy
        for _ in range(n+1): # move first pointer n steps ahead
            first = first.next
        while first: # move both pointers until first reaches the end
            first = first.next # move first pointer
            second = second.next# move second pointer
        second.next = second.next.next # remove the nth node from end
        return dummy.next # return the updated head
#example:
sll = SinglyLinkedList() # create singly linked list object
sll.head = Node(1) # create head node with data 1
sll.head.next = Node(2) # create second node with data 2
sll.head.next.next = Node(3) # create third node with data 3
sll.head.next.next.next = Node(4) # create fourth node with data 4
sll.head.next.next.next.next = Node(5) # create fifth node with data 5
n = 2 # nth node from end to be removed
new_head = sll.remove_nth_from_end(sll.head, n) # remove nth node from end
# print the updated linked list
current = new_head
while current:
    print(current.data, end=" -> " if current.next else "")
    current = current.next
'''tc = O(L) where L is the length of the linked list. We traverse the list
once.
sc = O(1) as we are using only constant extra space.'''

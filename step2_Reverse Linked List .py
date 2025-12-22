'''problem statement: explain the problem statement here
Given the head of a singly linked list, reverse the list, and return the reversed list.
#EXAMPLE:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Input: head = [1,2]
# Output: [2,1]'''
class Node:
    def __init__(self, data):#initializing a node
        self.data = data#data part of node
        self.next = None#pointer part of node
class SinglyLinkedList:#singly linked list class
    def __init__(self):#initializing head to None
        self.head = None#head of the linked list
#function to reverse the linked list
    def reverse_linked_list(self,head):#function to reverse thr linked list
        arr = [] # initialize an empty array to store the data of nodes
        temp = head # initialize temp to head to traverse the linked list
        while temp is not None: # traverse the linked list
            arr.append(temp.data) # append the data of each node to the array
            temp = temp.next # move to the next node
        arr.reverse() # reverse the array
        temp = head # reinitialize temp to head to traverse again
        i = 0 # initialize index to 0
        while temp is not None: #traverse the linked list again
            temp.data = arr[i] # assign the reversed data back to the nodes
            i += 1 # increment index
            temp = temp.next # move to the next node
        return head # return the head of the reversed linked list
#example:
sll = SinglyLinkedList() # create a singly linked list object
sll.head = Node(1) # create head node with data 1
sll.head.next = Node(2) # create second node with data 2
sll.head.next.next = Node(3) # create third node with data 3
sll.head.next.next.next = Node(4) # create fourth node with data 4
sll.head.next.next.next.next = Node(5) # create fifth node with data 5
reversed_head = sll.reverse_linked_list(sll.head) # reverse the linked list
# ✅ PRINT REVERSED LINKED LIST
result = []
current = reversed_head
while current is not None:
    result.append(current.data)
    current = current.next
print(result)   # OUTPUT: [5, 4, 3, 2, 1]
#optimized approach: in-place reversal
def reverse_linked_list_optimized(self,head):#function to reverse the linked list in-place
        prev = None # initialize previous pointer to None
        current = head # initialize current pointer to head
        while current is not None: # traverse the linked list
            next_node = current.next # store the next node
            current.next = prev # reverse the link
            prev = current # move previous pointer to current
            current = next_node # move current pointer to next node
        return prev # return the new head of the reversed linked list
#example:
sll_optimized = SinglyLinkedList() # create a singly linked list object
sll_optimized.head = Node(1) # create head node with data 1
sll_optimized.head.next = Node(2) # create second node with data 2
sll_optimized.head.next.next = Node(3) # create third node with data 3
sll_optimized.head.next.next.next = Node(4) # create fourth node with data
sll_optimized.head.next.next.next.next = Node(5) # create fifth node with data 5
reversed_head_optimized = reverse_linked_list_optimized(sll_optimized,sll_optimized.head) # reverse the linked list using optimized approach  
# ✅ PRINT REVERSED LINKED LIST
result_optimized = []
current_optimized = reversed_head_optimized
while current_optimized is not None:
    result_optimized.append(current_optimized.data)
    current_optimized = current_optimized.next
print(result_optimized)   # OUTPUT: [5, 4, 3, 2, 1]

'''Problem Statement
Given the head of a singly linked list and two integers left and right (1-indexed), reverse the nodes of the list from position left to position right, and return the modified list.
Only the nodes between left and right should be reversed.
All other nodes must remain unchanged.
#EXAMPLE:
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Input: head = [5], left = 1, right = 1
# Output: [5]
# Constraints:
# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
'''
#brute force approach: using extra space
class Node:
    def __init__(self, data):#initializing a node
        self.data = data#data part of node
        self.next = None#pointer part of node
class SinglyLinkedList:#singly linked list class
    def __init__(self):#initializing head to None
        self.head = None#head of the linked list
#function to reverse the linked list
    def reverse_linked_list(self,head,left,right):#function to reverse thr linked list
        arr = [] #initialize an empty array to store the data of nodes
        temp = head # initialize temp to head to traverse the linked list
        while temp is not None: # traverse the linked list
            arr.append(temp.data) # append the data of each node to the array
            temp = temp.next # move to the next node
            arr[left-1:right] = reversed(arr[left-1:right]) # reverse the subarray from left to right
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
reversed_head = sll.reverse_linked_list(sll.head,2,4) # reverse the linked list from position 2 to 4
# ✅ PRINT REVERSED LINKED LIST
result = []
current = reversed_head
while current is not None:
    result.append(current.data)
    current = current.next
print(result)   # OUTPUT: [1, 4, 3, 2, 5]
#optimized approach: in-place reversal
def reverse_linked_list_optimized(self,head,left,right):#function to reverse the linked list in-place
        if head is None:
            return None
        dummy = Node(0) # create a dummy node
        dummy.next = head # point dummy's next to head
        prev = dummy # initialize prev to dummy
        for _ in range(left - 1): # move prev to the node before left
            prev = prev.next
        current = prev.next # initialize current to the left node
        for _ in range(right - left): # reverse the sublist from left to right
            next_node = current.next # store the next node
            current.next = next_node.next # bypass the next node
            next_node.next = prev.next # insert next_node after prev
            prev.next = next_node # update prev's next to next_node
        return dummy.next # return the new head of the reversed linked list
#example:
sll_optimized = SinglyLinkedList() # create a singly linked list object
sll_optimized.head = Node(1) # create head node with data 1
sll_optimized.head.next = Node(2) # create second node with data 2
sll_optimized.head.next.next = Node(3) # create third node with data 3
sll_optimized.head.next.next.next = Node(4) # create fourth node with data 4
sll_optimized.head.next.next.next.next = Node(5) # create fifth node with data 5
reversed_head_optimized = reverse_linked_list_optimized(sll_optimized, sll_optimized.head, 2, 4) # reverse the linked list from position 2 to 4 using optimized approach
# ✅ PRINT REVERSED LINKED LIST
result_optimized = [] #
current_optimized = reversed_head_optimized
while current_optimized is not None:#
    result_optimized.append(current_optimized.data)
    current_optimized = current_optimized.next
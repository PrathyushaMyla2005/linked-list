'''problem statement:
You are given the head of a singly linked list.
Your task is to swap every two adjacent nodes in the list and return the head of the modified linked list
The swap must be done by changing node links, not by swapping values.
The operation should be performed pairwise:
1st node ↔ 2nd node
3rd node ↔ 4th node
and so on.
If the list contains an odd number of nodes, the last node remains unchanged.
If the list is empty or has only one node, return it as is.
#EXAMPLE:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]'''
#brute force approach: using extra space
class Node:
    def __init__(self, data):#initializing a node
        self.data = data#data part of node
        self.next = None#pointer part of node
class SinglyLinkedList:#singly linked list class
    def __init__(self):#initializing head to None
        self.head = None#head of the linked list
#function to swap nodes in pairs
    def swap_pairs(self,head):#function to swap nodes in pairs
        arr = [] #initialize an empty array to store the data of nodes
        temp = head # initialize temp to head to traverse the linked list
        while temp is not None: # traverse the linked list
            arr.append(temp.data) # append the data of each node to the array
            temp = temp.next # move to the next node
        for i in range(0, len(arr) - 1, 2): # iterate through the array in steps of 2
            arr[i], arr[i + 1] = arr[i + 1], arr[i] # swap adjacent elements
        temp = head # reinitialize temp to head to traverse again
        i = 0 # initialize index to 0
        while temp is not None: #traverse the linked list again
            temp.data = arr[i] # assign the swapped data back to the nodes
            i += 1 # increment index
            temp = temp.next # move to the next node
        return head # return the head of the modified linked list
#example:
sll = SinglyLinkedList() # create a singly linked list object
sll.head = Node(1) # create head node with data 1
sll.head.next = Node(2) # create second node with data 2
sll.head.next.next = Node(3) # create third node with data 3
sll.head.next.next.next = Node(4) # create fourth node with data 4
sll.head.next.next.next.next = Node(5) # create fifth node with data 5
swapped_head = sll.swap_pairs(sll.head) # swap nodes in pairs
# ✅ PRINT SWAPPED LINKED LIST
result = []# initialize an empty list to store the result
current = swapped_head# initialize current to the head of the swapped linked list
while current is not None:# traverse the linked list
    result.append(current.data)# append the data of each node to the result list
    current = current.next# move to the next node
print(result)   # OUTPUT: [2, 1, 4, 3, 5]
#optimized approach: in-place swapping
def swap_pairs_optimized(self,head):#function to swap nodes in pairs in-place
        dummy = Node(0) # create a dummy node
        dummy.next = head # point dummy's next to head
        prev = dummy # initialize prev to dummy
        while prev.next and prev.next.next: # traverse the linked list while there are at least two nodes ahead
            first = prev.next # first node to be swapped
            second = prev.next.next # second node to be swapped
            # Swapping
            first.next = second.next # point first's next to the node after second
            second.next = first # point second's next to first
            prev.next = second # point prev's next to second
            # Move prev to first for the next pair
            prev = first
        return dummy.next # return the head of the modified linked list
#example:
sll_optimized = SinglyLinkedList() # create a singly linked list object
sll_optimized.head = Node(1) # create head node with data 1
sll_optimized.head.next = Node(2) # create second node with data 2
sll_optimized.head.next.next = Node(3) # create third node with data 3
sll_optimized.head.next.next.next = Node(4) # create fourth node with data
sll_optimized.head.next.next.next.next = Node(5) # create fifth node with data 5
swapped_head_optimized = sll_optimized.swap_pairs_optimized(sll_optimized.head) # swap nodes in pairs in-place
# ✅ PRINT SWAPPED LINKED LIST OPTIMIZED
result_optimized = []# initialize an empty list to store the result
current_optimized = swapped_head_optimized# initialize current to the head of the swapped linked list
while current_optimized is not None:# traverse the linked list
    result_optimized.append(current_optimized.data)# append the data of each node to the result list
    current_optimized = current_optimized.next# move to the next node
print(result_optimized)   # OUTPUT: [2, 1, 4, 3, 5]
'''tc: O(n) where n is the number of nodes in the linked list. We traverse the linked list a constant number of times.
sc: O(1) for the optimized approach as we are not using any extra space that grows with input size. For the brute-force approach, the space complexity is O(n) due to the additional array used to store node values.
'''
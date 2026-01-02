'''problem statement:Problem Statement
You are given the head of a singly linked list.
Reorder the linked list so that the nodes are arranged in the following pattern:
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → … 
1 → 2 → 3 → 4
1 → 4 → 2 → 3'''
#brute force approach: using extra space
class Node:
    def __init__(self, data):#initializing a node
        self.data = data#data part of node
        self.next = None#pointer part of node
class SinglyLinkedList:#singly linked list class
    def __init__(self):#initializing head to None
        self.head = None#head of the linked list
#function to reorder the linked list
    def reorder_list(self, head):#function to reorder the linked list
        arr = [] #initialize an empty array to store the nodes
        temp = head # initialize temp to head to traverse the linked list
        while temp is not None: # traverse the linked list
            arr.append(temp) # append each node to the array
            temp = temp.next # move to the next node
        i, j = 0, len(arr) - 1 # initialize two pointers
        while i < j: # traverse until the two pointers meet
            arr[i].next = arr[j] # point the next of the node at i to the node at j
            i += 1 # move i forward
            if i == j: # if both pointers meet, break
                break
            arr[j].next = arr[i] # point the next of the node at j to the node at i
            j -= 1 # move j backward
        arr[i].next = None # set the next of the last node to None
        return head # return the head of the modified linked list
#example:
sll = SinglyLinkedList() # create a singly linked list object
sll.head = Node(1) # create head node with data 1
sll.head.next = Node(2) # create second node with data 2
sll.head.next.next = Node(3) # create third node with data 3
sll.head.next.next.next = Node(4) # create fourth node with data 4
sll.head.next.next.next.next = Node(5) # create fifth node with data 5
reordered_head = sll.reorder_list(sll.head) # reorder the linked list
# ✅ PRINT REORDERED LINKED LIST
result = []# initialize an empty list to store the result
current = reordered_head# initialize current to the head of the reordered linked list
while current is not None:# traverse the linked list
    result.append(current.data)# append the data of each node to the result list
    current = current.next# move to the next node
print(result)   # OUTPUT: [1, 5, 2, 4, 3]
#optimized approach: in-place reordering
def reorder_list_optimized(self, head):#function to reorder the linked list in-place
        if not head or not head.next: # if the list is empty or has only one node
            return head
        # Step 1: Find the middle of the linked list
        slow, fast = head, head # initialize two pointers
        while fast and fast.next: # traverse the linked list
            slow = slow.next # move slow by one
            fast = fast.next.next # move fast by two
        # Step 2: Reverse the second half of the linked list
        prev, curr = None, slow # initialize prev to None and curr to slow
        while curr: # traverse the second half
            next_temp = curr.next # store the next node
            curr.next = prev # reverse the link
            prev = curr # move prev forward
            curr = next_temp # move curr forward
        # Step 3: Merge the two halves
        first, second = head, prev # initialize two pointers to the start of each half
        while second.next: # traverse until the end of the second half
            temp1, temp2 = first.next, second.next # store the next nodes
            first.next = second # link first node to second
            second.next = temp1 # link second node to next of first
            first, second = temp1, temp2 # move both pointers forward
        return head # return the head of the modified linked list
#example:
sll_optimized = SinglyLinkedList() # create a singly linked list object
sll_optimized.head = Node(1) # create head node with data 1
sll_optimized.head.next = Node(2) # create second node with data 2
sll_optimized.head.next.next = Node(3) # create third node with data 3
sll_optimized.head.next.next.next = Node(4) # create fourth node with data 4
sll_optimized.head.next.next.next.next = Node(5) # create fifth node with data 5
reordered_head_optimized = sll_optimized.reorder_list_optimized(sll_optimized.head) # reorder the linked list in-place
# ✅ PRINT REORDERED LINKED LIST OPTIMIZED
result_optimized = []# initialize an empty list to store the result
current_optimized = reordered_head_optimized# initialize current to the head of the reordered linked list
while current_optimized is not None:# traverse the linked list
    result_optimized.append(current_optimized.data)# append the data of each node to the result list
    current_optimized = current_optimized.next# move to the next node
print(result_optimized)   # OUTPUT: [1, 5, 2, 4, 3]

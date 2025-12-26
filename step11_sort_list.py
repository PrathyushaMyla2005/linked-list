'''problem statement:You are given the head of a singly linked list.
Your task is to sort the linked list in ascending order and return the head of the sorted list.
Input
head → the first node of a singly linked list
The linked list may contain positive, negative, or zero values
🔹 Output
Return the head of the linked list after sorting all nodes in ascending order
Input:  4 → 2 → 1 → 3
Output: 1 → 2 → 3 → 4
'''
#brute force approch
# Definition of a linked list node
# This class represents ONE node in a singly linked list
class ListNode:
    def __init__(self, val=0, next=None):
        # val stores the data/value of the node
        self.val = val
        
        # next stores the address (reference) of the next node
        self.next = next


# --------- INPUT LINKED LIST ----------
# We are manually creating this linked list:
# 4 -> 2 -> 1 -> 3 -> None

# Create first node with value 4
head = ListNode(4)

# Create second node with value 2 and link it to first node
head.next = ListNode(2)

# Create third node with value 1 and link it to second node
head.next.next = ListNode(1)

# Create fourth node with value 3 and link it to third node
head.next.next.next = ListNode(3)


# --------- STEP 1: STORE VALUES IN ARRAY ----------
# Create an empty array to store linked list values
arr = []

# current pointer starts from head of the linked list
current = head

# Traverse the linked list until current becomes None
while current is not None:
    # Add current node's value into array
    arr.append(current.val)
    
    # Move current to the next node
    current = current.next


# At this point:
# arr = [4, 2, 1, 3]


# --------- STEP 2: SORT THE ARRAY ----------
# Sort the array in ascending order
arr.sort()

# Now:
# arr = [1, 2, 3, 4]


# --------- STEP 3: CREATE NEW SORTED LINKED LIST ----------
# Create a dummy node
# Dummy node helps us easily build a new linked list
dummy = ListNode(-1)

# current pointer starts from dummy node
current = dummy

# Loop through each value in the sorted array
for value in arr:
    # Create a new node with current value
    current.next = ListNode(value)
    
    # Move current to the newly created node
    current = current.next


# Now the new linked list looks like:
# dummy -> 1 -> 2 -> 3 -> 4 -> None


# --------- STEP 4: PRINT SORTED LINKED LIST ----------
# The real head of sorted list is dummy.next
sorted_head = dummy.next

# Start traversal from sorted_head
current = sorted_head

# Traverse the sorted linked list
while current is not None:
    # Print current node's value
    print(current.val, end=" -> ")
    
    # Move to the next node
    current = current.next

# Print None to indicate end of linked list
print("None")
'''tc '''
#optimal 
# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to merge two sorted linked lists
def merge(l1, l2):
    dummy = ListNode(-1)      # dummy node to simplify merging
    current = dummy

    # Compare nodes from both lists and attach smaller one
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # Attach remaining nodes
    if l1:
        current.next = l1
    if l2:
        current.next = l2

    return dummy.next         # return merged list head


# Function to sort linked list using merge sort
def sortList(head):
    # Base case: empty list or single node is already sorted
    if head is None or head.next is None:
        return head

    # -------- Step 1: Find middle of the list --------
    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # Split the list into two halves
    prev.next = None

    # -------- Step 2: Sort both halves --------
    left = sortList(head)
    right = sortList(slow)

    # -------- Step 3: Merge sorted halves --------
    return merge(left, right)

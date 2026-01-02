'''Problem Statement
You are given the head of a singly linked list and an integer k.
Your task is to rotate the linked list to the right by k positions and return the new head of the list.
Rotating the list to the right means that in each rotation, the last node of the list is moved to the front.
Input:head — the head node of a singly linked list
k — a non-negative integer representing the number of rotations
📤 Output:Return the head of the rotated linked list
head = 1 → 2 → 3 → 4 → 5
k = 2
Output:4 → 5 → 1 → 2 → 3'''
class Node: # Definition for singly-linked list.
    def __init__(self,data):#initalize the node
        self.data = data
        self.next = None
class SinglyLinkedList:#singly linked list class
    def __init__(self):#initializing head to None
        self.head = None#head of the linked list
    def rotate_right(self, head, k):#function to rotate the linked list
        if head is None or head.next is None or k == 0:#if the list is empty or has only one node or k is 0
            return head #return head as it is
        for _ in range(k):#rotate the list k times
            prev = None #initialize prev to None
            curr = head #initialize curr to head
            while curr.next is not None:#traverse to the end of the list
                prev = curr #move prev to curr
                curr = curr.next #move curr to next node
            curr.next = head #point the next of last node to head
            head = curr #update head to last node
            prev.next = None #set the next of second last node to None
        return head #return the head of the rotated list
#example:
sll = SinglyLinkedList() # create a singly linked list object
sll.head = Node(1) # create head node with data 1
sll.head.next = Node(2) # create second node with data 2
sll.head.next.next = Node(3) # create third node with data 3
sll.head.next.next.next = Node(4) # create fourth node with data 4
sll.head.next.next.next.next = Node(5) # create fifth node with data
k = 2 # number of rotations
rotated_head = sll.rotate_right(sll.head, k) # rotate the linked list
# ✅ PRINT ROTATED LINKED LIST
result = []# initialize an empty list to store the result
current = rotated_head# initialize current to the head of the rotated linked list
while current is not None:# traverse the linked list
    result.append(current.data)# append the data of each node to the result list
    current = current.next# move to the next node
print(result)   # OUTPUT: [4, 5, 1, 2, 3]
'''time complexity: O(n*k) where n is the number of nodes in the linked list and k is the number of rotations.
space complexity: O(1) as we are using constant space.'''
#optimized approach: single pass rotation
def rotate_right_optimized(self, head, k):#function to rotate the linked list in single pass
        if head is None or head.next is None or k == 0:#if the list is empty or has only one node or k is 0
            return head #return head as it is
        # Step 1: Compute the length of the linked list and make it circular
        length = 1 #initialize length to 1
        tail = head #initialize tail to head
        while tail.next: #traverse to the end of the list
            tail = tail.next #move tail to next node
            length += 1 #increment length
        tail.next = head #make the list circular
        # Step 2: Find the new tail and new head
        k = k % length #update k to be within the length of the list
        steps_to_new_head = length - k #calculate steps to new head
        new_tail = head #initialize new_tail to head
        for _ in range(steps_to_new_head - 1): #traverse to the new tail
            new_tail = new_tail.next #move new_tail to next node
        new_head = new_tail.next #new head is next of new tail
        new_tail.next = None #break the circular link
        return new_head #return the new head of the rotated list
#example:
sll = SinglyLinkedList() # create a singly linked list object
sll.head = Node(1) # create head node with data 1
sll.head.next = Node(2) # create second node with data 2
sll.head.next.next = Node(3) # create third node with data 3
sll.head.next.next.next = Node(4) # create fourth node with data 4
sll.head.next.next.next.next = Node(5) # create fifth node with data
k = 2 # number of rotations
rotated_head_optimized = sll.rotate_right_optimized(sll.head, k) #
# rotate the linked list using optimized approach
# ✅ PRINT ROTATED LINKED LIST
result_optimized = []# initialize an empty list to store the result
current_optimized = rotated_head_optimized# initialize current to the head of the rotated linked list
while current_optimized is not None:# traverse the linked list
    result_optimized.append(current_optimized.data)# append the data of each node to the result list
    current_optimized = current_optimized.next# move to the next node
print(result_optimized)   # OUTPUT: [4, 5, 1, 2, 3]
'''time complexity: O(n) where n is the number of nodes in the linked list.
space complexity: O(1) as we are using constant space.'''

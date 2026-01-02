'''problem statement:
Given the head of a singly linked list, group all the nodes with odd indices together followed by
the nodes with even indices, and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
You must solve the problem in O(1) extra space complexity and O(n) time complexity.
Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
'''
class Node:#Definition for singly-linked list.
    def __init__(self,data):    #initalize the node
        self.data = data #data of the node
        self.next = None #`pointer to the next node
class SinglyLinkedList:#singly linked list class
    def __init__(self):# initializing head to None
        self.head = None #head of the linked list
    def odd_even_list(self, head):#function to reorder the linked list
        if head is None or head.next is None: #if the list is empty or has only one node
            return head #return head as it is
        odd = [] #list to store odd indexed nodes
        even = [] #list to store even indexed nodes
        current = head #initialize current to head
        position = 1 #initialize position to 1
        while current is not None: #traverse the linked list
            if position % 2 != 0: #if position is odd
                odd.append(current.data) #append data to odd list
            else: #if position is even
                even.append(current.data) #append data to even list
            current = current.next #move to the next node
            position += 1 #increment position
        # Combine odd and even lists
        combined = odd + even #combine odd and even lists
        # Create a new linked list from the combined list
        new_head = Node(combined[0]) #create head node of new linked list
        current = new_head #initialize current to new head
        for value in combined[1:]: #traverse the combined list
            current.next = Node(value) #create new node and link it
            current = current.next #move to the next node
        return new_head #return the head of the reordered linked list
#example:
sll = SinglyLinkedList() # create a singly linked list object
sll.head = Node(1) # create head node with data 1
sll.head.next = Node(2) # create second node with data 2
sll.head.next.next = Node(3) # create third node with data 3
sll.head.next.next.next = Node(4) # create fourth node with data 4
sll.head.next.next.next.next = Node(5) # create fifth node with data 5
reordered_head = sll.odd_even_list(sll.head) # reorder the linked list
# ✅ PRINT REORDERED LINKED LIST
result = [] # initialize an empty list to store the result
current = reordered_head # initialize current to the head of the reordered linked list
while current is not None: # traverse the linked list
    result.append(current.data) # append the data of each node to the result list
    current = current.next # move to the next node
print(result)   # OUTPUT: [1, 3, 5, 2, 4]
'''time complexity: O(n) where n is the number of nodes in the linked list.
space complexity: O(n) as we are using extra space to store odd and even indexed nodes.'''
#optimized approach: in-place reordering
def odd_even_list_optimized(self, head):#function to reorder the linked list in-place
    if head is None or head.next is None: #if the list is empty or has only one node
        return head #return head as it is
    odd = head #initialize odd pointer to head
    even = head.next #initialize even pointer to second node
    even_head = even #store the head of even lis
    while even is not None and even.next is not None: #traverse the list
        odd.next = even.next #link odd node to the next odd node
        odd = odd.next #move odd pointer to next odd node
        even.next = odd.next #link even node to the next even node
        even = even.next #move even pointer to next even node
    odd.next = even_head #link the end of odd list to the head of even list
    return head #return the head of the reordered linked list
#example:
sll = SinglyLinkedList() # create a singly linked list object
sll.head = Node(1) # create head node with data 1
sll.head.next = Node(2) # create second node with data 2
sll.head.next.next = Node(3) # create third node with data 3
sll.head.next.next.next = Node(4) # create fourth node with data 4
sll.head.next.next.next.next = Node(5) # create fifth node with data 5
reordered_head_optimized = sll.odd_even_list_optimized(sll.head) # reorder the linked list using optimized approach
# ✅ PRINT REORDERED LINKED LIST
result_optimized = [] # initialize an empty list to store the result
current_optimized = reordered_head_optimized # initialize current to the head of the reordered linked list
while current_optimized is not None: # traverse the linked list
    result_optimized.append(current_optimized.data) # append the data of each node to the result list
    current_optimized = current_optimized.next # move to the next node
print(result_optimized)   # OUTPUT: [1, 3, 5, 2, 4]
'''time complexity: O(n) where n is the number of nodes in the linked list.
space complexity: O(1) as we are using constant space.'''

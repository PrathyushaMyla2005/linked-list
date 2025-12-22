'''problem statement: explain the problem statement here
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
Tortoise and Hare approach: means using two pointers to traverse the linked list at different speeds.
The slow pointer (tortoise) moves one step at a time, while the fast pointer
(frog) moves two steps at a time. When the fast pointer reaches the end of the list, the slow pointer will be at the middle node.
example:
Input: head = [1,2,3,4,5]
Output: [3,4,5] how came  to this output? where 1,2 are skipped and 3 is the middle node
example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6] how came  to this output? where 1,2,3 are skipped and 4 is the second middle node
#for even length linked list we return the second middle node
for odd length linked list we return the middle node
'''
#brute force approach: count the number of nodes in the linked list and then traverse to the middle node
class Node:
    def __init__(self, data):#initializing a node
        self.data = data#data part of node
        self.next = None#pointer part of node
class SinglyLinkedList:#singly linked list class
    def __init__(self):#initializing head to None
        self.head = None#head of the linked list
#traversing a singly linked list
    def middle_node(self,head):#function to find the middle node of the linked list self means the object of the class
        #head means the first node of the linked list why we use head as parameter because we can call this function with any node as head
        count = 0 # initialize count of nodes to store the number of nodes
        current  = head # initialize current to head to traverse the linked list
        while current is not None: #traverse the linkedlist to count the number of nodes
            count += 1 # increment count for each node to be counted
            current = current.next # move to the next node 
        mid = count // 2 # calculate the middle index
        current = head # reinitialize current to head to traverse again
        for i in range(mid): # traverse to the middle node
            current = current.next # move to the next node
        return current # return the middle node
#example:
sll = SinglyLinkedList() # create a singly linked list object
sll.head = Node(1) # create head node with data 1
sll.head.next = Node(2) # create second node with data 2
sll.head.next.next = Node(3) # create third node with data 3
sll.head.next.next.next = Node(4) # create fourth node with data 4
sll.head.next.next.next.next = Node(5) # create fifth node with data 5
middle = sll.middle_node(sll.head) # find the middle no
# ✅ PRINT FROM MIDDLE TO END
result = []
current = middle
while current is not None:
    result.append(current.data)
    current = current.next

print(result)   # OUTPUT: [3, 4, 5]
#optimized approach: tortoise and hare method
def middle_node_optimized(self,head):#function to find the middle node of the linked list using tortoise and hare method
        slow = head # initialize slow pointer to head
        fast = head # initialize fast pointer to head
        while fast is not None and fast.next is not None: # traverse the linked list until fast pointer reaches the end
            slow = slow.next # move slow pointer one step
            fast = fast.next.next # move fast pointer two steps
        return slow # when fast pointer reaches the end, slow pointer will be at the middle node
#example:
sll_optimized = SinglyLinkedList() # create a singly linked list object
sll_optimized.head = Node(1) # create head node with data 1
sll_optimized.head.next = Node(2) # create second node with data 2
sll_optimized.head.next.next = Node(3) # create third node with data 3
sll_optimized.head.next.next.next = Node(4) # create fourth node with data
sll_optimized.head.next.next.next.next = Node(5) # create fifth node with data 5
middle_optimized = middle_node_optimized(sll_optimized,sll_optimized.head) # find the middle node using optimized approach
# ✅ PRINT FROM MIDDLE TO END
result_optimized = []
current_optimized = middle_optimized
while current_optimized is not None:
    result_optimized.append(current_optimized.data)
    current_optimized = current_optimized.next
print(result_optimized)   # OUTPUT: [3, 4, 5]

'''iven the head of a singly linked list, return the node where the cycle begins.
If there is no cycle, return null.
A cycle exists if a node’s next pointer points to a previous node in the list.
⚠️ You are not allowed to modify the linked list.
Approach: Two Pointers (Floyd’s Algorithm)
Step 1: Detect Cycle
Use two pointers:
slow → moves 1 step
fast → moves 2 steps
If they meet → cycle exists
If fast reaches null → no cycle
3 → 2 → 0 → -4
    ↑         |
    └─────────┘
Node with value 2
'''
class Node:
    def __init__(self, data):#initializing a node
        self.data = data#data part of node
        self.next = None#pointer part of node
class SinglyLinkedList:#singly linked list class
    def __init__(self):
        self.head = None#head of the linked list
    def detect_cycle_start(self, head):#function to detect the start of cycle in linked
        slow = head # initializ  the head
        fast = head # initialize fast pointer to head
        # Step 1: Detect Cycle
        while fast and fast.next: # traverse the linked list
            slow = slow.next # move slow pointer by 1 step
            fast = fast.next.next # move fast pointer by 2 steps
            if slow == fast: # if both pointers meet, there is a cycle
                break
            else:
                return None # no cyclE
        # Step 2: Find Cycle Start
        slow = head # reset slow pointer to head
        while slow != fast: # traverse until both pointers meet
            slow = slow.next # move slow pointer by 1 step
            fast = fast.next # move fast pointer by 1 step
        return slow # return the node where the cycle begins
sll = SinglyLinkedList() # create a singly linked list object
sll.head = Node(3) # create head node with data 3
sll.head.next = Node(2) # create second node with data 2
sll.head.next.next = Node(0) # create third node with data 0
sll.head.next.next.next = Node(-4) # create fourth node with data -4
sll.head.next.next.next.next = sll.head.next # create a cycle by linking the
# last node to the second node
cycle_start_node = sll.detect_cycle_start(sll.head) # detect the start of the cycle
if cycle_start_node:
    print(cycle_start_node.data)   # OUTPUT: 2
else:
    print("No cycle detected")
'''tc = O(n) as in the worst case, we may need to traverse the entire list.
sc = O(1) as we are using only two pointers regardless of the input size.
'''


'''What is the problem?
In this problem, we are given two singly linked lists, say List A and List B.
We need to find the node where these two linked lists intersect.
👉 What does intersection mean?
Intersection means:
Both linked lists share the same node
It is not about same value
It is about same node in memory
After the intersection point, both lists continue as one list.
👉 What is given as input?
headA → head of first linked list
headB → head of second linked list
👉 What should we return?
Return the first common node where both lists meet
If the lists do not intersect, return null
👉 Example (to explain in interview)
List A: 1 → 2 → 3 → 4 → 5 → null
List B:       9 → 3 → 4 → 5 → null
Here:
Node 3 is the same node for both lists
So the intersection starts at node 3
Output: 3'''
#these problem we can solve by two pointer approach and hashset approach and linkedlist length approach
#hashset approach
class Node:
    def __init__(self, data):#initializing a node
        self.data = data#data part of node
        self.next = None#pointer part of node
class SinglyLinkedList:#singly linked list class
    def __init__(self):
        self.head = None#head of the linked list
    def get_intersection_node(self,headA, headB):#function to find intersection node of two linked list
        visted = set() # create an empty set to store visited nodes
        while headA: # traverse the first linked list
            visted.add(headA) # add each node to the set
            headA = headA.next # move to the next node
        while headB: # traverse the second linked list
            if headB in visted: # check if the current node is in the visited set
                return headB # if found, return the intersection node
            headB = headB.next # move to the next node
        return None # if no intersection is found, return None
#example:
sll1 = SinglyLinkedList() # create first singly linked list object
sll1.head = Node(1) # create head node with data 1
sll1.head.next = Node(2) # create second node with data 2
sll1.head.next.next = Node(3) # create third node with data 3
sll1.head.next.next.next = Node(4) # create fourth node with data
sll1.head.next.next.next.next = Node(5) # create fifth node with data 5
sll2 = SinglyLinkedList() # create second singly linked list object
sll2.head = Node(9) # create head node with data 9
sll2.head.next = sll1.head.next.next # create intersection at node with data 3
intersection_node = sll1.get_intersection_node(sll1.head, sll2.head) # find intersection node
if intersection_node:
    print(intersection_node.data)   # OUTPUT: 3
else:
    print("No intersection")
'''tc = O(m + n) where m and n are the lengths of the two linked
lists. We traverse each list once.
sc = O(m) where m is the length of the first linked list.
We store all nodes of the first list in a set.
'''
#linkedlist length approach
class Node:
    def __init__(self, data):#initializing a node
        self.data = data#data part of node
        self.next = None#pointer part of node
class SinglyLinkedList:#singly linked list class
    def __init__(self):
        self.head = None#head of the linked list
    def get_intersection_node(self,headA, headB):#function to find intersection
        if headA is None or headB is None: # if either list is empty
            return None # return None
        tempA = headA # initialize tempA to headA
        tempB = headB # initialize tempB to headB
        while tempA != tempB: # traverse until both pointers meet
            if tempA is None: # if tempA reaches the end of list A
                tempA = headB # switch to headB
            else:
                tempA = tempA.next # move to the next node in list A
            if tempB is None: # if tempB reaches the end of list B
                tempB = headA # switch to headA
            else:
                tempB = tempB.next # move to the next node in list B
        return headA # return the intersection node or None if no intersection
#example:
sll1 = SinglyLinkedList() # create first singly linked list object
sll1.head = Node(1) # create head node with data 1
sll1.head.next = Node(2) # create second node with data 2
sll1.head.next.next = Node(3) # create third node with data 3
sll1.head.next.next.next = Node(4) # create fourth node with data
sll1.head.next.next.next.next = Node(5) # create fifth node with data 5
sll2 = SinglyLinkedList() # create second singly linked list object
sll2.head = Node(9) # create head node with data 9
sll2.head.next = sll1.head.next.next # create intersection at node with data
intersection_node = sll1.get_intersection_node(sll1.head, sll2.head) # find intersection node
if intersection_node:
    print(intersection_node.data)   # OUTPUT: 3
else:
    print("No intersection")
'''tc = O(m + n) where m and n are the lengths of the two linked
lists. We traverse each list at most twice.
sc = O(1) as we are using only a constant amount of extra space.
'''
#two pointer approach
class Node:
    def __init__(self, data):#initializing a node
        self.data = data#data part of node
        self.next = None#pointer part of node
class SinglyLinkedList:#singly linked list class
    def __init__(self):
        self.head = None#head of the linked list
    def get_intersection_node(self,headA, headB):#function to find intersection
        slow = headA # initialize slow pointer to headA
        fast = headB # initialize fast pointer to headB
        while slow != fast: # traverse until both pointers meet
            if slow is None: # IF slow reaches the end of list A
                slow = headB # switch to headB
            else:
                slow = slow.next # move to the next node in list A
            if fast is None: # IF fast reaches the end of list B
                fast = headA # switch to headA
            else:
                fast = fast.next # move to the next node in list B
        return slow # return the intersection node or None if no intersection
#example:
sll1 = SinglyLinkedList() # create first singly linked list object
sll1.head = Node(1) # create head node with data 1
sll1.head.next = Node(2) # create second node with data 2
sll1.head.next.next = Node(3) # create third node with data 3
sll1.head.next.next.next = Node(4) # create fourth node with data
sll1.head.next.next.next.next = Node(5) # create fifth node with data 5
sll2 = SinglyLinkedList() # create second singly linked list object
sll2.head = Node(9) # create head node with data 9
sll2.head.next = sll1.head.next.next # create intersection at node with data
intersection_node = sll1.get_intersection_node(sll1.head, sll2.head) # find intersection node
if intersection_node:
    print(intersection_node.data)   # OUTPUT: 3
else:
    print("No intersection")
'''tc = O(m + n) where m and n are the lengths of the two linked
lists. We traverse each list at most twice.
sc = O(1) as we are using only a constant amount of extra space.
'''




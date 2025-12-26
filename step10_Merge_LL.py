'''you are given two singly linked lists, and both lists are already sorted in ascending order.
Your task is to merge these two lists into one single linked list, such that:
The final list is also sorted in ascending order
No new values are created unnecessarily
The merged list contains all nodes from both lists
Input
list1 → head of the first sorted linked list
list2 → head of the second sorted linked list
Each node contains:an integer value a pointer to the next 
Output
Return the head of the merged sorted linked list
Input:
list1 = 1 → 3 → 5 → null
list2 = 2 → 4 → 6 → null
Output:
1 → 2 → 3 → 4 → 5 → 6 → null
'''
#brute force approach  using array
class Node:
    def __init__(self, data):#initializing a node
        self.data = data#data part of node
        self.next = None#pointer part of node
class SinglyLinkedList:#singly linked list class
    def __init__(self):
        self.head = None#head of the linked list
    def merge_two_lists(self, list1, list2):#function to merge two sorted linked list
        arr = [] # create an empty array to store node values
        while list1: #traverse the first linkedlist
            arr.append(list1.data) # add each node's value to the array
            list1 = list1.next # move to the next node
        while list2: #traverse the second linkedlist
            arr.append(list2.data) # add each node's value to the array
            list2 = list2.next # move to the next node
        arr.sort() # sort the array
        dummy = Node(0) # create a dummy node to build the merged linked list
        current = dummy # initialize current pointer to dummy
        for value in arr: # create new nodes for each value in the sorted array
            current.next = Node(value) # create a new node and link it
            current = current.next # move to the next node
        return dummy.next # return the head of the merged linked list
#example:
sll1 = SinglyLinkedList() # create first singly linked list object
sll1.head = Node(1) # create head node with data 1
sll1.head.next = Node(3) # create second node with data 3
sll1.head.next.next = Node(5) # create third node with data 5
sll2 = SinglyLinkedList() # create second singly linked list object
sll2.head = Node(2) # create head node with data 2
sll2.head.next = Node(4) # create second node with data 4
sll2.head.next.next = Node(6) # create third node with data 6
merged_head = sll1.merge_two_lists(sll1.head, sll2.head) # merge the two linked lists
# print the merged linked list
current = merged_head
while current:
    print(current.data, end=" -> " if current.next else "")
    current = current.next
'''tc = O(m log m + n log n) where m and n are the lengths of the two linked
lists. We traverse both lists to collect values (O(m + n))
and then sort the combined list of values (O((m + n) log(m + n))).
sc = O(m + n) where m and n are the lengths of the two linked
lists. We store all node values in an array.
'''
# optimal approach  using pointers
class Node:
    def __init__(self, data):#initializing a node
        self.data = data#data part of node
        self.next = None#pointer part of node
class SinglyLinkedList:#singly linked list class
    def __init__(self):
        self.head = None#head of the linked list
    def merge_two_lists(self, list1, list2):#function to merge two sorted linked list
        dummy = Node(0) # create a dummy node to build the merged linked list
        current = dummy # initialize current pointer to dummy
        while list1 and list2: # traverse both lists until one is exhausted
            if list1.data < list2.data: # compare node values
                current.next = list1 # link the smaller node to the merged list
                list1 = list1.next # move to the next node in list1
            else:
                current.next = list2 # link the smaller node to the merged list
                list2 = list2.next # move to the next node in list2
            current = current.next # move to the next node in the merged list
        # link any remaining nodes from either list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        return dummy.next # return the head of the merged linked list
#example:
sll1 = SinglyLinkedList() # create first singly linked list object
sll1.head = Node(1) # create head node with data 1
sll1.head.next = Node(3) # create second node with data 3
sll1.head.next.next = Node(5) # create third node with data 5
sll2 = SinglyLinkedList() # create second singly linked list object
sll2.head = Node(2) # create head node with data 2
sll2.head.next = Node(4) # create second node with data 4
sll2.head.next.next = Node(6) # create third node with data 6
merged_head = sll1.merge_two_lists(sll1.head, sll2.head)
# print the merged linked list
current = merged_head
while current:
    print(current.data, end=" -> " if current.next else "")
    current = current.next
'''tc = O(m + n) where m and n are the lengths of the two linked lists.
We traverse both lists once.
sc = O(1) as we are only using a few pointers for merging the lists.
'''
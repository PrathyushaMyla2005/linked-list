'''Problem Statement (Format)
You are given the head of a sorted singly linked list.
Your task is to remove duplicate elements such that each value appears only once in the linked list.
Return the head of the modified linked list.
Inputhead → head of a sorted singly linked list
Return the head of the linked list after removing duplicate nodes
Example:
head = [1 → 1 → 2 → 3 → 3]
Output: [1 → 2 → 3]'''
class Node:
    def __init__(self, data):#initializing a node
        self.data = data#data part of node
        self.next = None#pointer part of node
class SinglyLinkedList:#singly linked list class
    def __init__(self):#initalizing head to None
        self.head = None#head of the linked list
    def remove_duplicates(self,head):#function to remove duplicates from sorted linked list
        if head is None: # if the linked list is empty
            return None# return None
        if head.next is None: # if the linked list has only one node
            return head# return head as there are no duplicates
        temp = head # initialize temp to head
        while temp.next is not None: # traverse the linked list
            if temp.data == temp.next.data: # if current node data is equal to next node data
                temp.next = temp.next.next # bypass the duplicate node by linking current node to the node after next
            else:
                temp = temp.next # move to the next node
        return head # return the head of the modified linked list
#example:
sll =SinglyLinkedList() # create a singly linked list object
sll.head = Node(1) # create head node with data 1
sll.head.next = Node(1) # create second node with data 1 (duplicate)
sll.head.next.next = Node(2) # create third node with data 2
sll.head.next.next.next = Node(3) # create fourth node with data 3
sll.head.next.next.next.next = Node(3) # create fifth node with data 3 (duplicate)
modified_head = sll.remove_duplicates(sll.head) # remove duplicates from the sorted linked list
# ✅ PRINT MODIFIED LINKED LIST
result = []
current = modified_head
while current is not None:
    result.append(current.data)
    current = current.next
print(result)   # OUTPUT: [1, 2, 3]
'''tc = O(n) as we may need to traverse the entire list in the worst case because we might have to check all nodes.
sc = O(1) as we are not using any extra space that grows with input size.
'''

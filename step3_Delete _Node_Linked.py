'''problem statement: explain the problem statement here
Given the head of a singly linked list and an integer val, delete the first occurrence of val in the linked list. Return the head of the modified linked list.
#EXAMPLE:
# Input: head = [4,5,1,9], val = 5
# Output: [4,1,9]
# Input: head = [4,5,1,9], val = 1
# Output: [4,5,9]
# Input: head = [1,2,3,4,5], val = 6
# Output: [1,2,3,4,5]'''
#class for a node in singly linked list
class Node:
    def __init__(self, data):#initializing a node
        self.data = data#data part of node
        self.next = None#pointer part of node
class SinglyLinkedList:#singly linked list class
    def __init__(self):#initializing head to None
        self.head = None#head of the linked list
    def delete_node(self,head,val):#function to delete a node with given values
        if head is None:# if the linked list is empty
            return None# return None
        if head.data == val:# if the head node is to be deleted
            return head.next# return the next node as new head
        temp = head# initialize temp to head
        while temp.next is not None:#traverse the linked list
            if temp.next.data == val:#if the next node is to be deleted
                temp.next = temp.next.next# bypass the node to be deleted
                return head# return the head of the modified linked list
                break # exit the loop after deletion
            temp = temp.next# move to the next node
        return head# return the head if node not found
#example:
sll =SinglyLinkedList() # create a singly linked list object
sll.head = Node(4) # create head node with data 4
sll.head.next = Node(5) # create second node with data 5
sll.head.next.next = Node(1) # create third node with data 1
sll.head.next.next.next = Node(9) # create fourth node with data 9
val_to_delete  = 5 # value to be deleted
modified_head = sll.delete_node(sll.head, val_to_delete) # delete the node with value 5
# ✅ PRINT MODIFIED LINKED LIST
result = []
current = modified_head
while current is not None:
    result.append(current.data)
    current = current.next
print(result)   # OUTPUT: [4, 1, 9]
'''tc = O(n) as we may need to traverse the entire list in the worst case because we might have to check all nodes.
sc = O(1) as we are not using any extra space that grows with input size.
'''
#optimized approach: using a dummy node to simplify deletion

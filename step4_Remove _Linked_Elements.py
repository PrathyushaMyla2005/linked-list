'''Problem Statement (One Format)
You are given the head of a singly linked list and an integer value val.
Your task is to remove all nodes from the linked list whose value is equal to val and return the modified linked list.
head → head of the singly linked list
val → integer value to be removed
Output:
Return the head of the updated linked list after removing all nodes with value val
head = [1 → 2 → 6 → 3 → 4 → 5 → 6]
val = 6
# Output: [1 → 2 → 3 → 4 → 5]'''
class Node:
    def __init__(self, data):#initializing a node
        self.data = data#data part of node
        self.next = None#pointer part of node
class SinglyLinkedList:#singly linked list class
    def __init__(self):#initalizing head to None
        self.head = None#head of the linked list
    def remove_elements(self,head,val):#function to remove elements with given value
        if head is None:# if the linked list is empty
            return None# return None
        # Remove nodes from the beginning if they match the value
        if head.data == val:
            return head.next# return the next node as new head
        temp = head# initialize temp to head
        while temp.next is not None:
            if temp.next.data == val:#if the next node is to be deleted
                temp.next = temp.next.next# bypass the node to be deleted
            else:
                temp = temp.next# move to the next node
        return head# return the head of the modified linked list
#example:
sll =SinglyLinkedList() # create a singly linked list object
sll.head = Node(1) # create head node with data 1
sll.head.next = Node(2) # create second node with data 2
sll.head.next.next = Node(6) # create third node with data 6
sll.head.next.next.next = Node(3) # create fourth node with data 3
sll.head.next.next.next.next = Node(4) # create fifth node with data 4
sll.head.next.next.next.next.next = Node(5) # create sixth node with data 5
sll.head.next.next.next.next.next.next = Node(6) # create seventh node with data 6
val_to_remove  = 6 # value to be removed
modified_head = sll.remove_elements(sll.head, val_to_remove) # remove nodes with value 6
# ✅ PRINT MODIFIED LINKED LIST
result = []
current = modified_head
while current is not None:
    result.append(current.data)
    current = current.next
print(result)   # OUTPUT: [1, 2, 3, 4, 5]
'''tc = O(n) as we may need to traverse the entire list in the worst case beacuse why o(n) means we might have to check all nodes. 
we cannot o(1) because we may need to check all nodes.
sc = O(1) as we are not using any extra space that grows with input size.
'''

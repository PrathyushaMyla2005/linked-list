'''problem statement:
Given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]'''
class Node:  # Definition for singly-linked list
    def __init__(self, data):# initialization of node
        self.data = data# data part
        self.next = None# pointer part

class SinglyLinkedList:# singly linked list class
    def __init__(self):# initialization of linked list
        self.head = None# head pointer
    def add_two_nodes(self, l1, l2):# function to add two linked list
        carry = 0                       # initialize carry
        result = Node(0)                # dummy node
        cur = result                    # pointer to result list
        while l1 or l2:                 # same condition as yours
            val = 0                     # initialize sum
            if l1:                      # add l1 value
                val += l1.data          # add l1 data to val
                l1 = l1.next            # move l1 forward
            if l2:                      # add l2 value
                val += l2.data          # add l2 data to val
                l2 = l2.next            # move l2 forward
            val += carry                # add carry
            if val > 9:                 # your carry logic
                carry = 1              # set carry
            else:                      # reset carry
                carry = 0               # reset carry

            cur.next = Node(val % 10)   # store digit
            cur = cur.next              # move result pointer

        # handle last carry (VERY IMPORTANT)
        if carry == 1:                # if carry is left
            cur.next = Node(1)              # add new node

        return result.next              # skip dummy
# Example usage:
l1 = SinglyLinkedList()            # first linked list
l1.head = Node(2)                  # first node
l1.head.next = Node(4)             # second node
l1.head.next.next = Node(3)        # third node
l2 = SinglyLinkedList()            # second linked list
l2.head = Node(5)                  # first node
l2.head.next = Node(6)             # second node
l2.head.next.next = Node(4)        # third node
result = SinglyLinkedList()        # result linked list
result.head = result.add_two_nodes(l1.head, l2.head)  # add two linked lists
# Print result
cur = result.head                  # pointer to result list
while cur:                         # traverse result list
    print(cur.data, end=" -> ")    # print data
    cur = cur.next                  # move forwad
print("None")                      # end of list
# Output: 7 -> 0 -> 8 -> None
'''tc = O(max(m,n)) where m and n are lengths of the two linked lists.
sc = O(max(m,n)) for the new linked list.'''

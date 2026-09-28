# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None # previous none as the start node dosent have a previous node
        current = head # always start at the beggining of the list  
                        #aka where the head points
        while current:   # loop until current is equal to None counting as false
            temp = current.next  # store the next node of the  node that
                                # that we are now 
            current.next = prev # change the current adress of the node to prev
            prev = current # store current in prev 
            current = temp # store temp in current 
                            #basically moving to the next node 
        return prev 
        

        
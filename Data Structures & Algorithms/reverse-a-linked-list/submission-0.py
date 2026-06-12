# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      
        #Stack for reversing
        stack = []

        #Check if head is None
        if head is None:
            return None

        temp = head
        
        #We store in stack
        while temp is not None:

            stack.append(temp)
            temp = temp.next
        
        # Now we pop and make a new LL
        # new head
        new_head = stack.pop(-1)
        temp = new_head


        while stack:

            if len(stack) == 1:
                temp.next = stack.pop(-1)
                temp.next.next = None
            else:
                temp.next = stack.pop(-1)
                temp = temp.next

            
        
        return new_head



        
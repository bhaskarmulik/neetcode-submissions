# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #Count the total
        count = 0
        curr = head

        while curr:

            count+=1
            curr = curr.next
        
        
        trav = count - n

        #Remove the nth element from the end
        curr = head
        prev = None

        while curr:

            if trav == 0:
                if prev == None:
                    return curr.next if not None else None
                prev.next = curr.next
                break
            trav -=1
            prev = curr
            curr = curr.next
        
        return head



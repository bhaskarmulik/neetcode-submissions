# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def find_middle(self, head : Optional[ListNode]) -> Optional[ListNode]:

        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        print(f"{slow.val}")
        return slow

    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        prev = None

        while curr:

            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        temp = prev
        while temp:
            print(f"{temp.val}")
            temp = temp.next
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:

        mid = self.find_middle(head)

        next_head = mid.next
        mid.next = None

        reorder_head = self.reverse_list(next_head)

        curr1 = head
        curr2 = reorder_head

        while curr1.next:

            nxt = curr1.next
            curr1.next = curr2
            curr2 = curr2.next
            curr1.next.next = nxt
            curr1 = curr1.next.next

        while curr2:
            curr1.next = curr2
            curr2 = curr2.next



        
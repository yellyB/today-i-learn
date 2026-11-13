# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = ListNode()
        large = ListNode()
        smallCurr = small
        largeCurr = large
        while head:
            if head.val < x:
                smallCurr.next = ListNode(head.val)
                smallCurr = smallCurr.next
            else:
                largeCurr.next = ListNode(head.val)
                largeCurr = largeCurr.next
            head = head.next
        smallCurr.next = large.next
        return small.next

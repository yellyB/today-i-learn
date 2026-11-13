# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = head  # 구한 합계를 업뎃하기 위한 포인터(slow)
        p2 = head.next  # 노드 순회해가면서 합계에 저장하기 위한 포인터(fast)
        sums = 0
        while p2:
            if p2.val:
                sums += p2.val
            else:
                p1 = p1.next
                p1.val = sums
                sums = 0
            p2 = p2.next
        p1.next = None
        return head.next

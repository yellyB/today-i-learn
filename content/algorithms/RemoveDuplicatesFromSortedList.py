# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        head.next = self.deleteDuplicates(head.next)

        # 현재값이 다음값이랑 같으면 중복이니까
        # 현재값 건너뛰고 그 다음값을 리턴해줌
        # 그게 아니면 걍 현재값 리턴
        return head.next if head.val == head.next.val else head
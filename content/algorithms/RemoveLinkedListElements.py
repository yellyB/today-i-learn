# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev, curr = None, head  # prev는 -1, curr은 0번 인덱스라고 생각하면 됨
        while curr:
            if curr.val == val:  # 현재포인터의 값이 제거해야 될 값이면
                # 근데 맨 처음은 prev가 없는 상태니까 검사 한번 해줌
                if prev:  # prev가 있으면(=제거해야될값이 첫빠따가 아니면)
                    prev.next = curr.next  # curr은 prev보다 한 포인터 뒤니까. 건너뛰고 붙여줌
                else:
                    head = curr.next  # 첫빠따면 걔 없애고 두번째꺼 붙임
                curr = curr.next  # 검사 끝났으면 한칸 다음꺼
            else:
                prev, curr = curr, curr.next  # 제거해야될 값 아니면 둘 다 한칸씩 다음꺼
        return head

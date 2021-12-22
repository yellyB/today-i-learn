# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

    # 뒤에서 n만큼 위치인 값을 빼려면 앞에서부터 전체-n 만큼 가면 된다.
    # fast로 n 만큼 갈거임. 그 위치부터 fast가 끝에 다다를때까지 slow를 같이 돌리면 전체-n만큼 갈 수 있음
    # 그 위치인거 건너뛰고 slow의 그 다음 노드를 이어 붙이면 됨

    # ***** 근데 16줄에서 head가 그 건너뛴 값으로 바뀌는데 이 부분을 모르겠음
    #       같은 포인터를 가리키고 있어서 그런거 같긴한데 확실히 이해가 잘 안감
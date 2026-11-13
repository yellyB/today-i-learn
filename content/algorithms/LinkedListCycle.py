# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        return False

    # 한 부분이 연결되어 있다면 하나는 +1씩, 다른 하나는 +2씩 포인터를 옮겨가다보면 결국에 만나는 순간이 있음
    # 연결된 부분 없다면 계속 돌지 못하고 while문 탈출하겠지
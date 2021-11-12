# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr) // 2]

    # arr에 일단 노드를 넣음
    # 젤 마지막 노드가 아닐때까지(next가 있을때까지) 돌려
    # 마지막 리스트의 next를 계속 arr에 추가해
    # 리스트의 중간을 반환하면 끝

    # slow = fast = head
    # while fast and fast.next:
    #     slow = slow.next
    #     fast = fast.next.next
    # return slow

    # 와 이거 개천재인듯 two pointer사용.
    # fast는 slow보다 두배 빠르게 노드를 탐색함.
    # fast가 끝에 다다랐다면 절반인 slow는 중간을 가리키고 있을 것

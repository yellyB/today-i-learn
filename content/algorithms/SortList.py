# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        queue = []  # 우선순위 큐
        pointer = head
        
        # 1. 우선순위 큐를 이용해서 모든 값들을 담는다.
        while pointer:
            heapq.heappush(queue, pointer.val)
            pointer = pointer.next
        
        # 2. 정답을 담을 노드 생성. 포인터는 정답을 가리키도록 세팅
        ans = ListNode()
        pointer = ans
        
        # 3. ans에 담아주기
        while queue:
            val = heapq.heappop(queue)  # 꺼낸걸
            pointer.next = ListNode(val)  # 노드 생성해서 다음포인터로
            pointer = pointer.next  # 다했으면 다음 포인터로 이동
        
        return ans.next  # 맨 첫값은 빈값을 넣었기때문에 next를 리턴해줌

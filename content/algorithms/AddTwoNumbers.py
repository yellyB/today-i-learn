# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sums = curr = ListNode()  # sums의 포인터로 사용하기 위해 curr 만듬
        temp = 0  # 올림할 수 저장 위한 변수
        
        while l1 or l2 or temp >= 1:  # l1과 l2가 없어도 올려줄 수가 있으면 계속해야함
            if l1:
                temp += l1.val
                l1 = l1.next
            if l2:
                temp += l2.val
                l2 = l2.next
                
            curr.next = ListNode(temp % 10)  # 일의자리만
            temp //= 10  # 올려줄 수만 남기기
            curr = curr.next  # 포인터 이동
            
        
        return sums.next  # 맨 처음에 생기는 0 무시하기 위해

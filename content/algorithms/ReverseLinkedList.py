# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 방법 1  -> 얘가 더 빠르넴
        new = None
        while head:
            temp = head.next  # 뒷부분 일단 빼놔
            head.next = new  # 헤드 다음꺼를 거꾸로 정렬한 애로 바꿔
            new = head  # 거꾸로정렬 리스트에 젤 앞에꺼 추가
            head = temp  # 헤드를 다시 잠깐빼놓은(맨앞은 빠진)애로
        return new

        # 방법2 재귀
        # def reverse(head, prev):
        #     if not head: return prev
        #     temp = head.next
        #     head.next = prev
        #     return reverse(temp, head)
        # return reverse(head, None)
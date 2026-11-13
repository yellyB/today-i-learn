# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 결국 갈수록 작은 값이어야 한다는거
        def remove(head):
            if not head:
                return None
                
            head.next = remove(head.next)

            if head.next and head.val < head.next.val:
                return head.next
            else:
                return head
        
        return remove(head)

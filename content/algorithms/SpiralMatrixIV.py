# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1] * n for _ in range(m)]
        r, c = 0, 0
        dr, dc = 0, 1

        while head:
            res[r][c] = head.val
            if r+dr < 0 or r+dr >= m or c+dc < 0 or c+dc >= n or res[r+dr][c+dc] != -1:
                dr, dc = dc, -dr
            r += dr
            c += dc
            head = head.next

        return res

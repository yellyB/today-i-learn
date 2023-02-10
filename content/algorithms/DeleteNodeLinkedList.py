# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val  # 값을 뒤에꺼 갖고와서 덮어씀
        node.next = node.next.next  # 값을 뒤에서 갖고왔기 때문에 원래 있던 뒤에 노드 값이랑 중복될테니까, 다음 노드도 땡김
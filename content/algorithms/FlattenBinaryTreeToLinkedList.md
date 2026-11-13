---
date: '2022-04-06'
---

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        '''
        [컨셉]
        노드가 붙는 순서가, val->left->right기 때문에
        현재 트리에서 right는 현재 트리 모든 left를 확인한 뒤에 그제서야 붙을거임.
        그러니까 right 는 left의 가장 마지막 우측에 붙이자
        '''
        while root:
            if root.left:
                currLeft = root.left
                # 1. 현재 트리 left의 가장 우측 찾기
                while currLeft.right:
                    currLeft = currLeft.right
                currLeft.right = root.right  # 2. 가장 우측 찾았으면 거기에 현재트리 right 붙이기

                root.right = root.left  # 3.  2번까지 작업한 left를 right에 붙여주기
                root.left = None  # 4. left 를 오른쪽에 붙여줬으니 left 는 비워줌
            root = root.right  # 5. 모든거 right에 붙였으니 다음 right 를 탐색 ㄱㄱ
```

```javascript
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {void} Do not return anything, modify root in-place instead.
 */
var flatten = function(root) {
    // 방법1 재귀
    let head = null;  // 오른쪽에 붙는 노드를 저장할 포인터. 지금까지 모은 오른쪽노드들
    const recursion=(root)=>{
        if(root.right) recursion(root.right);
        if(root.left) recursion(root.left);
        root.left = null;  // 왼편 비우고
        root.right = head;  // 오른편엔 지금까지 모은 노드를 붙여준다.
        head = root;  // root를 갱신했으니 head도 갱신
        
    }
    
    if(root) recursion(root)
    
    
    /*
    방법2 : [Morris Traversal]
    let curr = root;
    while(curr){
        if(curr.left){
            // 왼쪽 노드들의 가장 오른쪽에 현재node오른쪽 부분을 이어붙여야 하기 때문에 포인터 이동
            let l = curr.left;
            while(l.right) l = l.right;
            
            l.right = curr.right;  // 현재노드의 왼편중에서 가장 오른쪽에다가 현재오른노드를 붙여준다.
            curr.right = curr.left;  // 왼쪽노드를 오른쪽으로 이동
            curr.left = null;  // 왼쪽 비우기
        }
        curr = curr.right;  // 계속 오른쪽으로 넘어가면서 탐색. 왼쪽노드가 있을때마다 위의 루프 실행예정
    }
    */
};
```

---
date: '2021-11-20'
---

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def getCnt(node):
            if not node: return 0
            return max(getCnt(node.left), getCnt(node.right)) + 1
        return getCnt(root)
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
 * @return {number}
 */
var maxDepth = function(root) {
    const getCount=(root)=>{
        if(!root) return 0
        
        return Math.max(getCount(root.left), getCount(root.right)) + 1
    }
    
    return getCount(root)
};
```

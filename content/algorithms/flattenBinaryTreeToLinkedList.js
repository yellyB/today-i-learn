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
    let head = null;  // 오른쪽에 붙는 노드를 저장할 포인터. 지금까지 모은 오른쪽노드들
    const recursion=(root)=>{
        if(root.right) recursion(root.right);
        if(root.left) recursion(root.left);
        root.left = null;  // 왼편 비우고
        root.right = head;  // 오른편엔 지금까지 모은 노드를 붙여준다.
        head = root;  // root를 갱신했으니 head도 갱신
        
    }
    
    if(root) recursion(root)
    
};

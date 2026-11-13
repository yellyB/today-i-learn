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

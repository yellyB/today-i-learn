/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function insertIntoBST(root: TreeNode | null, val: number): TreeNode | null {
    // 암것도 없으면 val로 트리만들 ㄱㄱ
    if(!root){
        return new TreeNode(val)
    }

    const dfs = (thisRoot:TreeNode) => {
        if(thisRoot.val > val){
            if(thisRoot.left){  // 왼쪽에 노드 있으면 그거가지고 트리만들러
                dfs(thisRoot.left)
            }else {
                thisRoot.left = new TreeNode(val)  // 노드 없으면 아예 새 트리 만들어서 붙여줌
            }
        }else {
            if(thisRoot.right){
                dfs(thisRoot.right)
            }else {
                thisRoot.right = new TreeNode(val)
            }
        }
    }

    dfs(root)

    return root
};
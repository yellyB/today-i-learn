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
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
var isSubtree = function(root, subRoot) {
     
    // root랑 subRoot받아서 이 두 트리를 끝까지 검사했을 때 서브트리와 같은지
    const dfs = (root, subRoot) => {
        if( (root&&!subRoot) || (!root&&subRoot) ) return false;  // 둘 중 하나만 있으면 실패
        if(!subRoot) return true;  // 위 통과했는데 subRoot가 없다면 둘다 없다는뜻. 끝까지 검사한거니 성공

        // 두 값이 같으면 남은 subRoot도 체크
        if(root.val === subRoot.val){
            return dfs(root.left, subRoot.left) && dfs(root.right, subRoot.right)
        }else{
            return false;
        }
    }

    
    
    if(!root) return false; //넘기다가 null나오면 false리턴
    
    if(dfs(root, subRoot)){
        // dfs검사해서 subRoot를 찾았으면 true
        return true;
    }else{
        // 못찾았으면 root를 다음으로 넘어가서 또 비교
        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot)
    }
    
       
};

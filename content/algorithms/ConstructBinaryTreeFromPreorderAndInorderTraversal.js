/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function(preorder, inorder) {
    let pIdx = 0;  // pre-order의 인덱스. 루트가 하나씩 추가될때마다 다음껄로 넘어가야 해서 바깥에서 관리
    const getRoot=(start, end)=>{
        if(pIdx >= preorder.length) return null;
        if(start>end) return null
        
        const tree = new TreeNode(preorder[pIdx]);  // pre의 값이 곧 최상위 노드
        const rootIdx = inorder.indexOf(preorder[pIdx]); // pre의 root가 in에서의 위치
        pIdx ++;  // 새로운 루트 추가했으니 다음 루트를 찾으러 가야함
        
        tree.left = getRoot(start, rootIdx-1);
        tree.right = getRoot(rootIdx+1, end);
        
        return tree;
    }
    
    return getRoot(0, preorder.length-1);
    
};


/*
pre에서는 루트를 먼저 싹 순회하니까 pre의 순서대로 in-order의 루트를 결정할 수 있음
그리고 pre의 현재 idx는 in의 구분점이 될 수 있음
무슨뜻이냐면 pre의 [i]가 inOrder에서 위치하는 곳 기준 왼편 요소는 왼쪽 노드들, 오른편 요소는 오른쪽 노드를 구성함
이걸 재귀로 풀면 됨
*/

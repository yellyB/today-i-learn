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

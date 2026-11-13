/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function(head) {
    const recursion=(head)=>{
        if(!head) return null;
        if(!head.next) return head;
        
        const node = new ListNode(head.next.val);
        node.next = new ListNode(head.val);
        node.next.next = recursion(head.next.next)
        
        return node
    }
    
    
    return recursion(head)
};

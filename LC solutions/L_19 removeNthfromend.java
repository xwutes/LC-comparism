//LC 19 delete nth from end of llist
// public class ListNode {
//     int val;
//     ListNode next;
//     ListNode(){}
//     ListNode(int val) { this.val = val; }
//     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
// }
class Solution {
    // 主函数
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // 虚拟头结点
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        // 删除倒数第 n 个，要先找倒数第 n + 1 个节点
        ListNode left = dummy;  
        ListNode right = dummy;
        // 删掉倒数第 n 个节点
        for (int i = 0; i < n; i++) {
    
            right = right.next;
        }
        while (right.next != null) { // notice that the position is .next!!
            right = right.next;
            left = left.next;
        }
        left.next = left.next.next;
        return dummy.next;
}
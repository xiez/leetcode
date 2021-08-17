/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode oddEvenList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        
        ListNode head_next = head.next;
        ListNode i, j;
        i = head;
        j = head_next;
        
        while (i.next != null && j.next != null) {
            i.next = j.next;
            j.next = i.next.next;
            i = i.next;
            j = j.next;
        }
        
        i.next = head_next;
        return head;
    }
}

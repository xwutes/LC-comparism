#LC_143 reorderList
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Solution:
    def reorderList(self, head:ListNode) ->None:
        #find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse second half
        second = slow.next
        prev = slow.next = None             #set slow.next to null to break the list to two parts
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first, second = head, prev
        while second:                       # loop the second pointer till reaching null, which we previously set in line11
            tmp1, tmp2 = first.next, second.next
            first.next = second             # we could suppliment second by prev
            second.next = tmp1 
            first, second = tmp1, tmp2
            
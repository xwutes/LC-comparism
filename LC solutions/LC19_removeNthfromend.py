#LC19_removeNthfromend

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def removeNthfromend(self, head, n):    # two argument as input
        # if head is None:            notice that size of head is 1-30,
        #     return None             corner case does not including 0
        dummy = ListNode(0)         # initiate dummy 
        dummy.next = head           # join dummy to given list
        left = right = dummy

        for i in range(n):
            right = right.next
        while right.next:           # notice this position need .next 
            left = left.next        # both pointer should loop together
            right = right.next
        left.next = left.next.next
        return dummy.next
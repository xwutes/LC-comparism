# LC-comparism
daily routine for study DSA, comparing python &amp; Java
# 1.linkedlist
**LC21. merge sorted linkedlist**

Usually there will be a default setting of ListNode have two attributes: self.val and self.next

In python: so when initialize pointers of two sorted list could assign: l1,l2 = ListNode() to generate pointers respectively

In Java:  ListNode p1 = l1, p2 = l2;

**LC19. removeNthfromend**

Java declare variables: 


    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {

      ListNode dummy = new ListNode(-1), p = dummy;
                               
      ListNode p1 = l1, p2 = l2;
    ...
    }
as a static language, each variable should declare type

comparing with python:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        p = dummy
        
could declare type through type hints,which is not affecting run-time but could be detected by third-party-tools

reference:https://www.augmentedmind.de/2020/10/11/static-python-type-hints/

**LC206.ReverseList**

In python:

        if head is None or head.next is None:
            return head

notice if only have one if condition, there would be error of head attribute(next)

key manipulation in recurse case.
<img width="1211" alt="Screen Shot 2022-04-22 at 14 09 08" src="https://user-images.githubusercontent.com/92950517/164770860-7b5cc275-fdd1-4022-b34f-4d4a48fc9f14.png">
it demenstrate a regular method to reverse a pointer.

also there is a method to reverse list in limited window in LC92.

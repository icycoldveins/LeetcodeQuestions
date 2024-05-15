class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        while curr.next and curr.next.next:
            # firstnodetoconsider
            first = curr.next
            # secondnodetoconsider
            second = curr.next.next
            # set the current to what the second value is
            curr.next = second
            # firstnodewill point to what the second node is pointing to
            first.next = second.next
            # now we have to change what second node is pointing to, first
            second.next = first
            # current will now become the value just after second
            curr = curr.next.next

        return dummy.next

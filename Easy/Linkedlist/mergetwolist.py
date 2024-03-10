# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        # Initialize a dummy node as the head of the merged list
        dummy = ListNode()
        current = dummy

        # Initialize pointers for list1 and list2
        pointer1 = list1
        pointer2 = list2

        # Traverse both lists and compare values
        while pointer1 is not None and pointer2 is not None:
            if pointer1.val <= pointer2.val:
                current.next = pointer1
                pointer1 = pointer1.next  # move pointer1 forward
            else:
                current.next = pointer2
                pointer2 = pointer2.next  # move pointer2 forward
            current = current.next  # move current pointer forward

        # Append remaining nodes from list1 or list2
        # If one of the lists is not empty, link the rest of it to the merged list
        if pointer1 is not None:
            current.next = pointer1
        else:
            current.next = pointer2

        # Return the head of the merged list (excluding the dummy node)
        return dummy.next

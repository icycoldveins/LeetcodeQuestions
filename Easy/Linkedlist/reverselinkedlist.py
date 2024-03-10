class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head

        while current:
            next_node = current.next # Save the next node
            current.next = prev      # Reverse the current node
            prev = current           # Move prev to the current node
            current = next_node      # Move current to the next node
        return prev


""" class Solution(object):
    def reverseList(self, head):
        
        :type head: ListNode
        :rtype: ListNode
        
        # Base case: If the list is empty or has only one node, return the head.
        if not head or not head.next:
            return head
        
        # Recursively reverse the rest of the list.
        reversed_head = self.reverseList(head.next)
        
        # Change the next pointer of the current node to point to the previous node.
        head.next.next = head
        head.next = None
        
        return reversed_head
 """

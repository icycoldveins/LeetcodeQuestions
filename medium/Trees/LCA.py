class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode   
        :type q: TreeNode
        :rtype: TreeNode
        """
        current_node = root

        while current_node:
            # If both p and q are greater than current, they lie in right subtree.
            if p.val > current_node.val and q.val > current_node.val:
                current_node = current_node.right

            # If both p and q are lesser than current, they lie in left subtree.
            elif p.val < current_node.val and q.val < current_node.val:
                current_node = current_node.left

            # We've found the split point, i.e., the LCA node.
            else:
                return current_node

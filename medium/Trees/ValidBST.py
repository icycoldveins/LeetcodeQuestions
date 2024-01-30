# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.prev = None  # Previous node in in-order traversal

        def validate(node):
            if not node:
                return True  # An empty tree is a valid BST

            # Validate the left subtree
            if not validate(node.left):
                return False

            # Check current node's value against the previous node's value
            if self.prev and self.prev.val >= node.val:
                return False

            self.prev = node  # Update the previous node

            # Validate the right subtree
            return validate(node.right)

        return validate(root)

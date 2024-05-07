# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        # Base case: if the current node is None, just return None
        if root is None:
            return None

        # Recursively invert the left and right subtrees
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        # Swap the left and right subtrees
        root.left, root.right = right, left

        # Return the root of the inverted tree
        return root
        
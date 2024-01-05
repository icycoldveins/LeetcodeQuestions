# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.max_diameter = 0

        def depth(node):
            if not node:
                return 0
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            # Update the maximum diameter
            self.max_diameter = max(
                self.max_diameter, left_depth + right_depth)
            # Return the depth of the tree at this node
            return max(left_depth, right_depth) + 1

        depth(root)
        return self.max_diameter

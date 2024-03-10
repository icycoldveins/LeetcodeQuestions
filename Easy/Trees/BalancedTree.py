# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            return 1 + max(left_height, right_height)

        return height(root) != -1
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

    def isBalanced2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        l = self.depth(root.left)
        r = self.depth(root.right)
        return (abs(l-r) < 2) and self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, node):
        if node == None:
            return 0
        return max(self.depth(node.left), self.depth(node.right))+1

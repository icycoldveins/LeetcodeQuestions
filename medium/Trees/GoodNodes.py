class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def goodNodes(self, root):
        def dfs(node, max_val):
            if not node:
                return 0
            count = 0
            if node.val >= max_val:
                count += 1  # Current node is good
            max_val = max(max_val, node.val)  # Update max_val for the path
            count += dfs(node.left, max_val)  # Check left subtree
            count += dfs(node.right, max_val)  # Check right subtree
            return count

        return dfs(root, float('-inf'))  # Start DFS with negative infinity as initial max_val

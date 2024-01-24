# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        # If the tree is empty, return an empty list
        if not root:
            return []

        # Initialize a queue and add the root node to it
        queue = [root]
        result = []

        # Loop until the queue is empty
        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            level_nodes = []  # List to store values of nodes at this level

            for i in range(level_size):
                node = queue.pop(0)  # Remove the first node from the queue
                # Add the node's value to the list
                level_nodes.append(node.val)

                # Add the node's children to the queue for future processing
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Add the current level's values to the result
            result.append(level_nodes)

        return result

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k):
        # Initialize count and result variables
        self.count = 0
        self.result = None

        def inorder(node):
            if node and self.result is None:  # Check if node exists and result is not found yet
                inorder(node.left)  # Visit left subtree

                self.count += 1  # Increment count for each node visited
                if self.count == k:  # If count matches k, store the node's value as the result
                    self.result = node.val
                    return  # Return early since the kth element is found

                inorder(node.right)  # Visit right subtree

        inorder(root)  # Start the in-order traversal from the root
        return self.result  # Return the result after traversal

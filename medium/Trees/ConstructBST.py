class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        # Base case: If either of the lists is empty, return None.
        if not preorder or not inorder:
            return None
        
        # Step 1: Pop the root node from the preorder list.
        root_val = preorder.pop(0)
        
        # Step 2: Find the index of root_val in the inorder list.
        root_index = inorder.index(root_val)
        
        # Step 3: Create the root node.
        root = TreeNode(root_val)
        
        # Recursively construct left and right subtrees.
        root.left = self.buildTree(preorder, inorder[:root_index])
        root.right = self.buildTree(preorder, inorder[root_index + 1:])
        
        # Step 4: Return the root node.
        return root


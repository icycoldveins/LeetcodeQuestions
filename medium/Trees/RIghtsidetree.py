class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []  # If the tree is empty, return an empty list

        result = []  # This list will store the right side view
        queue = [root]  # Initialize the queue with the root node

        while queue:  # As long as there are nodes to process
            level_length = len(queue)  # Number of nodes at the current level
            for i in range(level_length):  # Iterate over these nodes
                node = queue.pop(0)  # Remove the first node in the queue

                if i == level_length - 1:  # If it's the last node of this level
                    result.append(node.val)  # Append its value to result

                if node.left:
                    # Add left child to queue if exists
                    queue.append(node.left)
                if node.right:
                    # Add right child to queue if exists
                    queue.append(node.right)

        return result  # Return the list of rightmost nodes at each level

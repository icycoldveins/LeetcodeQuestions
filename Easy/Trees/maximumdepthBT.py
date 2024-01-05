class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return max(left_depth, right_depth) + 1
""" Sure, let's consider an example of an unbalanced binary tree to demonstrate the steps in the recursion of the `maxDepth` function. We'll use the following unbalanced tree as an example:

```
    1
   / \
  2   3
 /     \
4       5
       / \
      6   7
```

Here's how the recursion would work step by step:

1. **Initial Call**: `maxDepth(1)`

2. **Processing Node 1**:
   - Recursive call to left child: `maxDepth(2)`
   - Recursive call to right child: `maxDepth(3)`

3. **Processing Node 2**:
   - Recursive call to left child: `maxDepth(4)`
   - Recursive call to right child: `maxDepth(null)` (no right child)
   - `maxDepth(4)` returns 1 (base case reached, leaf node)
   - `maxDepth(null)` returns 0 (base case for null node)
   - `maxDepth(2)` returns `max(1, 0) + 1 = 2`

4. **Processing Node 3**:
   - Recursive call to left child: `maxDepth(null)` (no left child)
   - Recursive call to right child: `maxDepth(5)`
   - `maxDepth(null)` returns 0
   - Processing Node 5:
     - Recursive call to left child: `maxDepth(6)`
     - Recursive call to right child: `maxDepth(7)`
     - Both `maxDepth(6)` and `maxDepth(7)` return 1 (both are leaf nodes)
     - `maxDepth(5)` returns `max(1, 1) + 1 = 2`
   - `maxDepth(3)` returns `max(0, 2) + 1 = 3`

5. **Back to Initial Call**:
   - `maxDepth(1)` now calculates the max depth of its left and right subtrees.
   - It returns `max(2, 3) + 1 = 4`

So, the maximum depth of this unbalanced binary tree is 4. The recursion navigates through each branch, calculating the depth by adding 1 for each level, and then combines these results to find the maximum depth. """
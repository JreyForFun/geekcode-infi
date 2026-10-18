# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
===============================================================================
VISUALIZATION OF EXECUTION FLOW & CALL STACK
===============================================================================

Example Tree (targetSum = 22):

         5
        / \
       4   8
      /   / \
     11  13  4
    /  \      \
   7    2      1

Step-by-Step Recursive Walkthrough:
-------------------------------------------------------------------------------
hasPathSum(Node(5), targetSum = 22)
|-- Node 5 is internal. Deduct 5. Remaining targetSum = 17.
|-- Calls: LEFT(Node(4), 17) OR RIGHT(Node(8), 17)
|
|---> [LEFT] hasPathSum(Node(4), targetSum = 17)
|     |-- Node 4 is internal. Deduct 4. Remaining targetSum = 13.
|     |-- Calls: LEFT(Node(11), 13) OR RIGHT(None, 13)
|     |
|     |---> [LEFT] hasPathSum(Node(11), targetSum = 13)
|     |     |-- Node 11 is internal. Deduct 11. Remaining targetSum = 2.
|     |     |-- Calls: LEFT(Node(7), 2) OR RIGHT(Node(2), 2)
|     |     |
|     |     |---> [LEFT] hasPathSum(Node(7), targetSum = 2)
|     |     |     |-- Node 7 IS A LEAF.
|     |     |     |-- Leaf check: targetSum(2) - root.val(7) == 0  -->  False
|     |     |     |-- RETURNS: False
|     |     |
|     |     |---> [RIGHT] hasPathSum(Node(2), targetSum = 2)
|     |           |-- Node 2 IS A LEAF.
|     |           |-- Leaf check: targetSum(2) - root.val(2) == 0  -->  True!
|     |           |-- RETURNS: True (Valid path found: 5 -> 4 -> 11 -> 2)
|     |     |
|     |     |-- Node 11 receives: False (left) OR True (right)  -->  RETURNS: True
|     |
|     |-- Node 4 receives: True from left child  -->  RETURNS: True (short-circuits)
|
|-- Node 5 receives: True from left child  -->  RETURNS: True (right branch 8 skipped!)

FINAL OUTPUT: True
===============================================================================
"""

class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        # 1. Base Case: If we traverse past a leaf into a null node, this path is invalid.
        if not root:
            return False

        # 2. Leaf Node Check: A node is a leaf if it has no left or right children.
        # If we are at a leaf, check if subtracting its value from the remaining sum yields exactly 0.
        if not root.left and not root.right:
            return targetSum - root.val == 0
        
        # 3. Path Continuation: If it's not a leaf, deduct the current node's value
        # from the target sum to pass the updated requirement to the child nodes.
        targetSum -= root.val

        # 4. Recursive Traversal: Explore down the left and right branches.
        # The 'or' operator provides short-circuiting: if the left branch finds a valid 
        # path and returns True, the right branch is completely ignored and True propagates up.
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
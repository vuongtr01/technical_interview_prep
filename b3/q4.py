# https://leetcode.com/problems/diameter-of-binary-tree/description/
# Time: O(n) n: number of nodes
# Space: O(n)
# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [0, 0]

            maxHeight = 0
            maxDiameter = 0
            newDiameter = 0

            if node.left:
                leftNodeValues = dfs(node.left)
                newDiameter += leftNodeValues[0]
                maxDiameter = max(maxDiameter, leftNodeValues[1])
                maxHeight = max(maxHeight, leftNodeValues[0])

            if node.right:
                rightNodeValues = dfs(node.right)
                newDiameter += rightNodeValues[0]
                maxDiameter = max(maxDiameter, rightNodeValues[1])
                maxHeight = max(maxHeight, rightNodeValues[0])

            maxDiameter = max(maxDiameter, newDiameter)

            return [maxHeight + 1, maxDiameter]

        return dfs(root)[1]

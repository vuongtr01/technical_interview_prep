# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Time: O(logn) n = number of nodes
# Space: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            return self.lowestCommonAncestor(root, q, p)

        if root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

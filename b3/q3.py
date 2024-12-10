# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# Time: O(nlogn) n: number of nodes
# Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
    
        nodeList = []

        def dfs(root, row, col):
            nodeList.append((col, row, root.val))
            if root.left:
                dfs(root.left, row + 1, col - 1)
            if root.right:
                dfs(root.right, row + 1, col + 1)
                
        dfs(root, 0, 0)
        nodeList.sort(key= lambda node: (node[0], node[1], node[2]))

        currentCol = nodeList[0][0]
        res = [[nodeList[0][2]]]
        for i in range(1, len(nodeList)):
            if nodeList[i][0] != currentCol:
                res.append([])
                currentCol = nodeList[i][0]
            
            res[-1].append(nodeList[i][2])

        return res
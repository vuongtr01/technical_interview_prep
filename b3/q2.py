# https://leetcode.com/problems/binary-search-tree-iterator/
# Time: O(1)
# Space: O(n) n: number of nodes
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.nodeList = []
        self.traverse(root)
        self.nextIndex = -1

    def traverse(self, root):
        if root.left:
            self.traverse(root.left)
        self.nodeList.append(root.val)

        if root.right:
            self.traverse(root.right)

    def next(self) -> int:
        self.nextIndex += 1
        return self.nodeList[self.nextIndex]

    def hasNext(self) -> bool:
        return self.nextIndex < len(self.nodeList) - 1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
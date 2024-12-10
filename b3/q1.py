# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Time: O(n) n = number of nodes
# Space: O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        def dfs(node, currentString):
            valueString = str(node.val)
            currentString += (str(len(valueString)) + valueString)
            if node.left:
                currentString += "1"
                currentString = dfs(node.left, currentString)
            else:
                currentString += "0"

            if node.right:
                currentString += "1"
                currentString = dfs(node.right, currentString)
            else:
                currentString += "0"

            return currentString
        return dfs(root, "")

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def dfs(decodedString, index):
            valueLength = int(decodedString[index])
            index += 1
            if decodedString[index] == "-":
                index += 1
                value = - int(decodedString[index: (index + valueLength - 1)])
                index += (valueLength - 1)
            else:
                value = int(decodedString[index: index + valueLength])
                index += valueLength
            newNode = TreeNode(value)
            if decodedString[index] == "1":
                index += 1
                leftNode, index = dfs(decodedString, index)
                newNode.left = leftNode
            else:
                index += 1

            if decodedString[index] == "1":
                index += 1
                rightNode, index = dfs(decodedString, index)
                newNode.right = rightNode
            else:
                index += 1
            return (newNode, index)
        if data == "":
            return None
        return dfs(data, 0)[0]


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
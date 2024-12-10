# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# Time: O(n) n: number of nodes
# Space: O(1)

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        leftMostPointer = root
        
        while leftMostPointer != None:
            runningPointer = leftMostPointer

            while runningPointer != None and runningPointer.left:
                runningPointer.left.next = runningPointer.right

                if runningPointer.next:
                    runningPointer.right.next = runningPointer.next.left

                runningPointer = runningPointer.next

            leftMostPointer = leftMostPointer.left

        return root
        

# Definition for a Node.
# Time: O(n) n: number of nodes
# Space: O(1)
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        leftMostPointer = root
        
        while leftMostPointer != None:
            runningPointer = leftMostPointer

            while True:
                if runningPointer.left:
                    runningPointer.left.next = runningPointer.right

                    if runningPointer.next:
                        runningPointer.right.next = runningPointer.next.left
                        runningPointer = runningPointer.next
                    else:
                        runningPointer.next = leftMostPointer.left
                        break
                else:
                    break

            leftMostPointer = leftMostPointer.left

        return root

n7 = Node(7)
n6 = Node(6)
n5 = Node(5)
n4 = Node(4)
n3 = Node(3, n6, n7)
n2 = Node(2, n4, n5)
n1 = Node(1, n2, n3)

def printNode(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
        
    print(res)
    
s = Solution()

printNode(s.connect(n1))
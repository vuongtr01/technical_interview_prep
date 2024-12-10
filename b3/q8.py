# https://leetcode.com/problems/minimum-height-trees/
# Time: O(E + V) E: number of edges, V: number of nodes
# Space: O(n) number of nodes

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        neighbors = defaultdict(list)
        edgesCount = defaultdict(int)
        leaves = deque()

        for n1, n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)
            edgesCount[n1] += 1
            edgesCount[n2] += 1

        for i in range(n):
            if edgesCount[i] == 1:
                leaves.append(i)

        while n > 2:
            for i in range(len(leaves)):
                node = leaves.popleft()
                
                for j in neighbors[node]:
                    edgesCount[j] -= 1
                    if edgesCount[j] == 1:
                        leaves.append(j)
                
                n -= 1

        res = []
        for i in leaves:
            res.append(i)

        return res
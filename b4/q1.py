# https://leetcode.com/problems/shortest-path-in-binary-matrix/
# Time: O(n^2)
# Space: O(n^2)

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[n-1][n-1] == 1 or grid[0][0] == 1:
            return -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1)]
        res = 1
        q = deque()
        q.append((0, 0))
        visited = set()
        visited.add((0, 0))

        while len(q) > 0:
            size = len(q)
            for i in range(size):
                currRow, currCol = q.popleft()
                if currRow == n-1 and currCol == n-1:
                    return res

                for dr, dc in directions:
                    newR, newC = currRow + dr, currCol + dc

                    if newR < 0 or newR >= n or newC < 0 or newC >= n:
                        continue

                    if (newR, newC) not in visited and grid[newR][newC] == 0:
                        q.append((newR, newC))
                        visited.add((newR, newC))
            res += 1
        return -1
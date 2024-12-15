# https://leetcode.com/problems/shortest-path-to-get-all-keys/
# Time: O(m*n* 26!)
# Space: O(m*n*26!)
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        rows, cols = len(grid), len(grid[0])
        countKeys = 0
        startRows, startCols = 0, 0
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j].islower():
                    countKeys += 1
                elif grid[i][j] == "@":
                    startRows, startCols = i, j

        steps = 0
        q = deque([(startRows, startCols, 0)])
        visited = set([(startRows, startCols, 0)])

        while q:
            for _ in range(len(q)):
                x, y, keyset = q.popleft()

                if grid[x][y].islower():
                    rep = ord(grid[x][y]) - ord("a")
                    if (keyset >> rep) & 1 == 0:
                        keyset = keyset ^ (1 << rep)
            
                if keyset == (2 ** countKeys - 1):
                    return steps

                for dx, dy in dirs:
                    i, j = x + dx, y + dy
                    if i < 0 or i >= rows or j < 0 or j >= cols:
                        continue
                    newChar = grid[i][j]
                    if newChar == "#" or (i, j, keyset) in visited:
                        continue
                    if newChar.isupper():
                        lock = ord(grid[i][j]) - ord("A")
                        if keyset & (1 << lock) == 0:
                            continue
                    q.append((i, j, keyset))
                    visited.add((i, j, keyset))
            steps += 1
        return -1
                    
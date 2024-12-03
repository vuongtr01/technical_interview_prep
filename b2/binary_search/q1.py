# https://leetcode.com/problems/swim-in-rising-water/
# time: O(n^2 log(n^2)) n = len(grid)
# Space: O(n^2)

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        size = len(grid)
        left = 0
        right = size * size
        res = size * size
        def canReach(time):
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            if grid[0][0] > time:
                return False
            queue = deque()

            queue.append((0, 0))
            visited = []
            visited.append((0, 0))

            while len(queue) > 0:
                r, c = queue.pop()

                if (r, c) == (size -1, size-1):
                    return True

                for dr, dc in directions:
                    newR = r + dr
                    newC = c + dc

                    if (newR >= 0 and newR < size and newC >= 0 and newC < size and (newR, newC) not in visited and grid[newR][newC] <= time):
                        queue.append((newR, newC))
                        visited.append((newR, newC))

            return False
        while left <= right:
            mid = (left + right) // 2

            if canReach(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res

        
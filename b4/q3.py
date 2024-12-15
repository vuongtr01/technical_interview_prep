# https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/
# Time: O((m*n) * 2^(m * n))
# Space: O(2^(m*n))

class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        numberOfBits = rows * cols
        finalState = 0
        startState = 0

        for r in range(rows):
            for c in range(cols):
                index = r * cols + c
                if mat[r][c] == 1:
                    startState = startState ^ (1 << ((numberOfBits - index - 1)))
        if startState == finalState:
            return 0
        res = 0
        q = deque()
        visited = set()
        q.append(startState)
        visited.add(startState)

        while len(q) > 0:
            res += 1
            size = len(q)

            for _ in range(size):
                currentState = q.popleft()

                for i in range(numberOfBits):
                    # print("choose index: ", i)
                    newState = currentState ^ (1 << (numberOfBits - i - 1))

                    # flip the left neihbor
                    if i % cols != 0:
                        newState = newState ^ (1 << (numberOfBits - (i-1) - 1))
                    
                    # flip the right neighbor
                    if i % cols != (cols - 1):
                        newState = newState ^ (1 << (numberOfBits - (i+1) - 1))

                    # flip the above neighbor:
                    if i - cols >= 0:
                        newState = newState ^ (1 << (numberOfBits - (i - cols) - 1))

                    # flip the below neighbor
                    if i + cols < numberOfBits:
                        newState = newState ^ (1 << (numberOfBits - (i + cols) - 1))

                    if newState == finalState:
                        return res

                    if newState not in visited:
                        q.append(newState)
                        visited.add(newState)
        return -1
        
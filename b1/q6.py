# https://leetcode.com/problems/range-sum-query-2d-immutable/description/
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefixSum = [[0 for _ in range(cols+ 1)] for _ in range(rows + 1)]

        for r in range(rows):
            currentSum = 0
            for c in range(cols):
                currentSum += matrix[r][c]
                self.prefixSum[r+1][c+1] = currentSum + self.prefixSum[r][c+1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefixSum[row2 + 1][col2 + 1] - self.prefixSum[row2 + 1][col1] - self.prefixSum[row1][col2 + 1] + self.prefixSum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
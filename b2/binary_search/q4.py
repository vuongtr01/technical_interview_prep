#https://leetcode.com/discuss/interview-question/341247/facebook-leftmost-column-index-of-1
# Time: O(mlogn)
# Space: O(m)
# m: number of rows
# n: number of cols
from bisect import bisect_right
def left_most_column(matrix):
    oneIndex = []
    
    for r in matrix:
        oneIndex.append(bisect_right(r, 0))
        
    leftMostOne = min(oneIndex)
    
    return leftMostOne if leftMostOne < len(matrix[0]) else -1

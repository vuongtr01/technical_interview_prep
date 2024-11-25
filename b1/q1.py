# https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0 for _ in range(1001)]

        for numP, fr, to in trips:
            diff[fr] += numP
            diff[to] -= numP
        actualValue = [0 for _ in range(1001)]
        actualValue[0] = diff[0]
        for i in range(0, 1001):
            actualValue[i] = actualValue[i-1] + diff[i]

            if actualValue[i] > capacity:
                return False

        return True
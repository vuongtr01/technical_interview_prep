# https://leetcode.com/problems/subarray-sums-divisible-by-k/description/
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remaindersCount = {0: 1}
        currentSum = 0
        res = 0

        for n in nums:
            currentSum += n
            remain = currentSum % k

            if remain in remaindersCount:
                res += remaindersCount[remain]
            else:
                remaindersCount[remain] = 0

            remaindersCount[remain] += 1
        return res
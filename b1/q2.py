# https://leetcode.com/problems/contiguous-array/description/
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """

        [1, 2, 3, 4,  5,  6]
        [1, 3, 6, 10, 15, 21]
        sum i -> j = prefix[j] - prefix[i-1]
        prefixSum0[i]: number of 0 from index 0 -> i inclusive
        prefixSum1[i]: number of 1 from index 0 -> i inclusive
        fixed j -> find min i such as: 
            prefixSum0[j] - prefixSum0[i] == prefixSum1[j] - prefixSum1[i]
        ->  prefixSum0[j] - prefixSum1[j] == prefixSum0[i] - prefixSum1[i]
        -> prefixSum diff at j == prefixSum dif at i
        """
        size = len(nums)
        res = 0
        diffMap = {0: -1}
        prefixSum0 = [0 for _ in range(size + 1)]
        prefixSum1 = [0 for _ in range(size + 1)]

        for i in range(size):
            if nums[i] == 0:
                prefixSum0[i] = prefixSum0[i-1] + 1
                prefixSum1[i] = prefixSum1[i-1]
            else:
                prefixSum1[i] = prefixSum1[i-1] + 1
                prefixSum0[i] = prefixSum0[i-1]

            diff = prefixSum0[i] - prefixSum1[i]

            if diff in diffMap:
                res = max(res, i - diffMap[diff])
            else:
                diffMap[diff] = i
        return res
        
# https://leetcode.com/problems/continuous-subarray-sum/description/
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        prefixSum[i]: nums[0] + ... + nums[i]
        fixed j -> find if exists i such as:
            prefixSum[j] % k == prefix[i] % k 
        """
        remainders = {}
        currentSum = 0

        for i in range(len(nums)):
            currentSum += nums[i]

            if currentSum % k == 0 and i >= 1:
                return True

            remainder = currentSum % k
            if remainder in remainders:
                if i - remainders[remainder] + 1 > 2:
                    return True
            else:
                remainders[remainder] = i
        return False
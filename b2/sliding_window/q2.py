#https://leetcode.com/problems/minimum-size-subarray-sum/
# Time: O(n)
# Space: O(1)

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        currentSum = 0
        res = len(nums) + 1
        while right < len(nums):
            currentSum += nums[right]

            while currentSum >= target:
                res = min(res, right - left + 1)

                currentSum -= nums[left]
                left += 1
            right += 1
        return res if res < len(nums) + 1 else 0
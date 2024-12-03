#https://leetcode.com/problems/find-the-longest-equal-subarray/
#Time: O(n) n: len(nums)
#Space: O(n) n: len(nums)

class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        countNumbers = defaultdict(int)
        currentMaxCount = 0
        left = 0
        right = 0
        res = 0
        while right < len(nums):
            countNumbers[nums[right]] += 1

            if countNumbers[nums[right]] >= countNumbers[currentMaxCount]:
                currentMaxCount = nums[right]

            while right - left + 1 - countNumbers[currentMaxCount] > k:
                countNumbers[nums[left]] -= 1
                left += 1

                if countNumbers[nums[left]] >= countNumbers[currentMaxCount]:
                    currentMaxCount = nums[left]


            res = max(res, countNumbers[currentMaxCount])
            right += 1

        return res
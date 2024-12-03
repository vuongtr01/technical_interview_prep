# https://leetcode.com/problems/subarrays-with-k-different-integers/
# Time: O(n)
# Space: O(n)

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        countDistinct = 0
        countNumbers = defaultdict(int)
        lastIndex = defaultdict(int)
        left = 0
        right = 0
        mid = 0
        res = 0

        while right < len(nums):
            if countNumbers[nums[right]] == 0:
                countDistinct += 1

            countNumbers[nums[right]] += 1
            lastIndex[nums[right]] = right

            while countDistinct > k:
                countNumbers[nums[left]] -= 1

                if countNumbers[nums[left]] == 0:
                    countDistinct -= 1
                left += 1
                mid = left
            if countDistinct == k:
                while lastIndex[nums[mid]] != mid:
                    mid += 1
                res += (mid - left + 1)
            right += 1

        return res 
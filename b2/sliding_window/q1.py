#https://leetcode.com/problems/count-number-of-nice-subarrays/description/
# Time complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        countOdds = 0
        left = 0
        right = 0
        firstOdd = 0
        res = 0

        while right < len(nums):
            if nums[right] % 2 == 1:
                countOdds += 1

            if countOdds > k:
                firstOdd += 1
                left = firstOdd
                countOdds -= 1

            if countOdds == k:
                while nums[firstOdd] % 2 != 1:
                    firstOdd += 1
                
                res += (firstOdd - left + 1)

            right += 1
        return res
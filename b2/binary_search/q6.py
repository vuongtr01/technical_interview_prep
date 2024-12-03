#https://leetcode.com/problems/split-array-largest-sum/
#Time: O(nlogm) n: len(nums) m = sum(nums) - max(nums)
#Space: O(1)

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        l = max(nums)
        r = sum(nums)

        def canBuildValidSubarrays(largestSum):
            numsOfSub = 0
            currentSum = 0

            for n in nums:
                currentSum += n
                if currentSum > largestSum:
                    numsOfSub += 1
                    currentSum = n

            numsOfSub += 1

            if numsOfSub > k:
                return False

            return True

        while l <= r:
            mid = (l + r) // 2

            if canBuildValidSubarrays(mid):
                r = mid - 1
            else:
                l = mid + 1

        return l
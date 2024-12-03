#https://leetcode.com/problems/house-robber-iv/
# Time: O(mlogn) m: len(nums) n: max(nums) - min(nums)
# Space: O(1)

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left = min(nums)
        right = max(nums)

        def isPossibleToRobKHouses(capability):
            countRob1 = 0
            countRob2 = 0

            for n in nums:
                if n <= capability:
                    temp = max(countRob1 + 1, countRob2)
                    countRob1 = countRob2
                    countRob2 = temp
                else:
                    countRob1 = countRob2

            return countRob2 >= k
        
        while left <= right:
            mid = (left + right) // 2

            if isPossibleToRobKHouses(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
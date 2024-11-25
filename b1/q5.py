# https://leetcode.com/problems/product-of-array-except-self/description/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        prefix = [1 for _ in range(size + 1)]
        surfix = [1 for _ in range(size + 1)]
        res = [1 for _ in range(size)]

        for i in range(size):
            prefix[i] = prefix[i-1] * nums[i]
        
        for i in range(size - 1, -1, -1):
            surfix[i] = surfix[i+1] * nums[i]

        for i in range(size):
            res[i] = prefix[i-1] * surfix[i+1]

        return res
#https://leetcode.com/problems/sliding-window-maximum/description/
# Time: O(n)
# Space: O(n)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        left = 0
        right = 0
        queue = deque()

        while right < len(nums):
            while len(queue) > 0 and nums[right] >= nums[queue[-1]]:
                queue.pop()

            queue.append(right)

            while right - left + 1 > k:
                if len(queue) > 0 and left == queue[0]:
                    queue.popleft()
                left += 1

            if right - left + 1 == k:
                res.append(nums[queue[0]])
            right += 1

        return res
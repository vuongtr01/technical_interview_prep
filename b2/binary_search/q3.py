# https://leetcode.com/problems/random-pick-with-weight/
# Time: O(logn)
# Space: O(n)

class Solution:

    def __init__(self, w: List[int]):
        self.prefixSum = [w[0]]

        for w in w[1:]:
            self.prefixSum.append(self.prefixSum[-1] + w)
        
        self.total_sum = self.prefixSum[-1]

    def pickIndex(self) -> int:
        target = random.random() * self.total_sum
        return bisect_left(self.prefixSum, target)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
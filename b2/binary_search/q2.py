#https://leetcode.com/problems/most-profit-assigning-work/
# Time: O((n+m)logn)
# Space: O(n)
# n = len(difficulty) m = len(worker)

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = [[profit[i], difficulty[i]] for i in range(len(difficulty))]
        jobs.sort(key= lambda job: job[0])

        for i in range(len(jobs) - 2, -1, -1):
            jobs[i][1] = min(jobs[i][1], jobs[i+1][1])

        res = 0

        def findJob(ability):
            maxProfit = 0
            left = 0
            right = len(jobs) - 1

            while left <= right:
                mid = (left + right) // 2

                if jobs[mid][1] <= ability:
                    maxProfit = jobs[mid][0]
                    left = mid + 1
                else:
                    right = mid - 1

            return maxProfit

        for w in worker:
            res += findJob(w)

        return res


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        memo = {}

        def f(i):
            if i == 0: return cost[0]
            if i == 1: return cost[1]
            if i in memo: return memo[i]

            here = cost[i] if i < n else 0
            memo[i] = min(f(i - 1), f(i - 2)) + here
            return memo[i]

        return f(n)
            
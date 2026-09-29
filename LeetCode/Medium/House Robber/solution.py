class Solution:
    def rob(self, nums: list[int]) -> int:
        memo = {}
        n = len(nums) - 1

        def dp(n):
            if n == 0:
                return nums[0]
            if n == 1:
                return max(nums[1], nums[0])
            if n in memo:
                return memo[n]

            memo[n] = max(dp(n - 1), dp(n - 2) + nums[n])
            return memo[n]
        
        return dp(n)

        
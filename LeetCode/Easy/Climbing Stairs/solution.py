class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n + 1)
        def dp(n):
            if n == 0 or n == 1:
                return 1
            if memo[n] != 0:
                return memo[n]
            
            memo[n] = dp(n - 1) + dp(n - 2)
            return memo[n]
        
        return dp(n)
    


        
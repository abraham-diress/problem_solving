class Solution:
    def minCost(self, height: list[int]) -> int:
        # code here
        n = len(height) - 1
        memo = [-1 for _ in range(n + 1)]
        
        
        def dp(n):
            if n <= 0:
                return 0
            if n == 1:
                return abs(height[1] - height[0])
            if memo[n] != -1:
                return memo[n]
            
            left = dp(n - 1) + abs(height[n] - height[n - 1])
            right = dp(n - 2) + abs(height[n] - height[n - 2])
            
            memo[n] = min(left, right)
            return memo[n]
        
        return dp(n)
        
        
        
        
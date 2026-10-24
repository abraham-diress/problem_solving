class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        def ways(i):
            if i == len(s):
                return 1 

            if s[i] == '0':
                return 0
            
            if i in dp:
                return dp[i]
            
            choice1 = ways(i + 1)

            choice2 = 0
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                choice2 = ways(i + 2)
            
            dp[i] = choice1 + choice2
            return dp[i]
        
        return ways(0)
        
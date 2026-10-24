class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = {}
        def canBreak(i):
            if i == len(s):
                return True 
            if i in dp:
                return dp[i]
            
            for word in wordDict:
                if s[i : i+len(word)] == word:
                    if canBreak(i + len(word)):
                        dp[i] = True
                        return dp[i]
            
            dp[i] = False
            return dp[i]
                        
        
        return canBreak(0)

        
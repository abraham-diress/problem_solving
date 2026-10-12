class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)
        max_len = 0

        for i in range(len(s)):
            if s[i] == ')':
                prevIndex = i - 1

                if i > 0 and dp[i - 1] > 0:
                    prevIndex -= dp[i - 1]

                if prevIndex >= 0 and s[prevIndex] == '(':
                    dp[i] = i - prevIndex + 1

                if prevIndex > 0 and dp[i] > 0 and dp[prevIndex - 1] > 0:
                    dp[i] += dp[prevIndex - 1]

                max_len = max(max_len, dp[i])

        return max_len
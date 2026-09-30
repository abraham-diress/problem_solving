class Solution:
    def fib(self, n: int) -> int:
        prev2 = 0
        prev1 = 1

        for i in range(n):
            prev2, prev1 = prev1, prev1 + prev2

        return prev2
        
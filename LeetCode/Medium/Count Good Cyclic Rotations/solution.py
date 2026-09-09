class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n = len(nums)
        half = n // 2

        total = sum(nums)

        window_sum = sum(nums[:half])
        answer = 0 

        for i in range(n):
            if window_sum > total - window_sum:
                answer += 1

            out = nums[i]
            incoming = nums[(i + half) % n]

            window_sum -= out 
            window_sum += incoming

        return answer       
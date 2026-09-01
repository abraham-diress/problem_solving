class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        l = 0 
        win_sum = 0 

        for r in range(len(nums)):
            win_sum += nums[r]

            while win_sum >= target:
                res = min(res, r - l + 1)

                win_sum -= nums[l]
                l += 1
        
        return res if res != float('inf') else 0  


        
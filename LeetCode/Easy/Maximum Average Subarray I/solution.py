class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        l = 0
        cur_sum = sum(nums[:k]) 
        max_avg = cur_sum / k

        for r in range(k, len(nums)):
            cur_sum -= nums[l]  
            cur_sum += nums[r]
            max_avg = max(max_avg, (cur_sum / k)) 
            l += 1
        
        return max_avg



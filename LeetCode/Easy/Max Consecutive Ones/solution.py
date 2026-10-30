class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        r = 0
        max_window = 0
        cur_window = 0
        nums.append(0)  

        while r < len(nums):
            if nums[r] == 1:
                cur_window += 1
                r += 1
            else:
                max_window = max(max_window, cur_window)
                r += 1
                cur_window = 0
        
        return max_window





        
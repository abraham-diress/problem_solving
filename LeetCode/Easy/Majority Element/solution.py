class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        balanced = 0
        candidate = nums[0]
        
        for num in nums:
            if num == candidate:
                balanced += 1
            elif balanced == 0:
                candidate = num
                balanced += 1
            else:
                balanced -= 1
        
        return candidate
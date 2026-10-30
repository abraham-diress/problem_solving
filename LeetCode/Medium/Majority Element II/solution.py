class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        hash_map = Counter(nums)
        repeat = len(nums) / 3
        ans = []

        for key, val in hash_map.items():
            if val > repeat:
                ans.append(key)
            
        return ans



        
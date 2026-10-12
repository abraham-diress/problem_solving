class Solution:

    def maxSum(self, nums, left, right):

        if left == right:
            return nums[left]

        mid = left + (right - left) // 2

        left_sum = 0
        left_best = nums[mid]

        i = mid

        while i >= left:
            left_sum += nums[i]
            left_best = max(left_best, left_sum)
            i -= 1

        right_sum = 0
        right_best = nums[mid + 1]

        j = mid + 1

        while j <= right:
            right_sum += nums[j]
            right_best = max(right_best, right_sum)
            j += 1

        crossing_sum = left_best + right_best

        left_result = self.maxSum(nums, left, mid)
        right_result = self.maxSum(nums, mid + 1, right)

        return max(left_result, right_result, crossing_sum)

    def maxSubArray(self, nums):

        if len(nums) == 1:
            return nums[0]

        return self.maxSum(nums, 0, len(nums) - 1)
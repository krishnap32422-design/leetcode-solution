class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum=0
        total=sum(nums)
        for right in range(len(nums)):
            right_sum=total-left_sum-nums[right]
            if left_sum==right_sum:
                return right
            left_sum+=nums[right]

        return -1
        
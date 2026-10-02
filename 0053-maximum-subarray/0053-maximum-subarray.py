class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum=0
        max_sum=nums[0]
        for right in range(len(nums)):
            curr_sum+=nums[right]

            max_sum=max(curr_sum,max_sum)
            if curr_sum<0:
                curr_sum=0
        return max_sum
         
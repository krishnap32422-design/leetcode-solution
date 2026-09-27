class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left=0
        n=len(nums)
        curr_sum=0
        min_size=float('inf')
        for right in range(n):
            curr_sum+=nums[right]

            while curr_sum>=target:
                min_size=min(min_size,right-left+1)
                curr_sum-=nums[left]
                left+=1

        if min_size==float('inf'):
            return 0
        else:
            return min_size
        
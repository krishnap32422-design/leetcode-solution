class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left=1
        right=max(nums)
        while left<=right:
            mid=(left+right)//2
            Smallest_Divisor=self.canDivisor(nums,mid)
            if Smallest_Divisor<=threshold:
                right=mid-1
            else:
                left=mid+1
        return left

        
    def canDivisor(self,nums,mid):
        divisor=0
        for i in range(len(nums)):
            divisor+=(nums[i]+mid-1)//mid
        return divisor
        
    
        
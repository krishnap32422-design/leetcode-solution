class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
         n=len(nums)
         left=0
         right=len(nums)-1
         while left<right:
            mid= left+(right-left+1)//2

            if nums[mid]>nums[mid-1]:
                left=mid
            else:
                 right=mid-1
         return  right
            

        
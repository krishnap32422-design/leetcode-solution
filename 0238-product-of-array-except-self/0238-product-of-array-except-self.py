class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans=[1]*len(nums)
        prefix_product=1
        for i in range(len(nums)):
            ans[i]=prefix_product

            prefix_product*=nums[i]
        suffix_product=1
        for j in range(len(nums)-1,-1,-1):
            ans[j]*=suffix_product
            suffix_product*=nums[j]
        
        return ans

        
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_product=float('-inf')
        prefix_product=1
        suffix_product=1
        for right in range(len(nums)):
            if prefix_product==0:

                prefix_product=1
            if suffix_product==0:
                suffix_product=1
            prefix_product*=nums[right]
            suffix_product*=nums[len(nums)-1-right]

            max_product=max(max_product,prefix_product,suffix_product)
        return max_product

            
        
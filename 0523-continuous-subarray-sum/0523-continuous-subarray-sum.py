class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        n=len(nums)
        prefix_sum=0
        dict1={0:-1}
        for right in range(n):
            prefix_sum+=nums[right]
            rem=prefix_sum%k
            if rem in dict1:
                if right-dict1[rem]>=2:
                    return True
            else:
                dict1[rem]=right

        return False
        
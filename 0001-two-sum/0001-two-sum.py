class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
           dict1={}
           n=len(nums)
           for i in range (n):
            total=target-nums[i]
            if total in dict1 :
                return (dict1[total],i)
            dict1[nums[i]]=i
        
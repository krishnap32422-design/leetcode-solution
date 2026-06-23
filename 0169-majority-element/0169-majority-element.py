class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        candidates=None
        for num in nums:
            if count==0:
                candidates=num
            if num==candidates:
                count+=1
            else:
                count-=1
        return candidates


            
        
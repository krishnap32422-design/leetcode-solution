class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        hashmap={0:1}
        count=0
        prefix_sum=0
        for i in range(len(nums)):
            prefix_sum+=nums[i]
            rem=prefix_sum%k
            if rem in hashmap:
                count+=hashmap[rem]
            hashmap[rem]=hashmap.get(rem,0)+1
        return count

        
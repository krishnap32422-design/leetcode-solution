from collections import defaultdict
class Solution:
    def totalFruit(self, nums: list[int]) -> int:
        freq=defaultdict(int)
        max_count=0
        left=0
        for right in range(len(nums)):
            freq[nums[right]]+=1

            while len(freq)>2:
                freq[nums[left]]-=1

                if freq[nums[left]]==0:
                    del freq[nums[left]]

                left+=1

            max_count=max(max_count,right-left+1)
        return max_count
        
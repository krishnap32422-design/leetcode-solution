from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
      def mostk(k):
        dict1=defaultdict(int)
        count=0
        left=0
        for right in range(len(nums)):
            dict1[nums[right]]+=1

            while len(dict1)>k:
                dict1[nums[left]]-=1

                if dict1[nums[left]]==0:
                    del dict1[nums[left]]
                left+=1
            count+=right-left+1

        return count
      return mostk(k)-mostk(k-1)

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count=k
        for i in range(len(arr)):
            if arr[i]<=count:
                count+=1
        return count
            
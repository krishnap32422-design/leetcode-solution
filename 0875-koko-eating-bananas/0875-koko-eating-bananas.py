class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        while left<=right:
            mid=(left+right)//2
            total_hour=self.can_finish(piles,mid)

            if total_hour<=h:
                right=mid-1
            else:left=mid+1

        return left

    def can_finish(self,piles:List[int],k):
        hours=0
        for pile in piles:
            hours+=(pile + k-1)//k
        return hours
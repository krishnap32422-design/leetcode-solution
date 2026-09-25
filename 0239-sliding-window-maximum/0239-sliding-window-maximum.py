from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq=deque()
        left=0
        result=[]
        for right in range(len(nums)):
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            dq.append(right)
            if dq[0]<left:
                dq.popleft()
            if right+1>=k:
                result.append(nums[dq[0]])
                left+=1
        return result

        
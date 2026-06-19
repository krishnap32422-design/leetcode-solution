class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if  self.check_target(matrix[i],target)==True:
                return True
        return False

    def check_target(self,matrix,target):
        left=0
        right=len(matrix)-1
        while left<=right:
            mid=(left+right)//2
            if matrix[mid]==target:
                return True
            elif matrix[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return False
        
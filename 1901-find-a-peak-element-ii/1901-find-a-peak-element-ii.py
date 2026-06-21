class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n=len(mat)
        m=len(mat[0])
        low=0
        high=m-1
        while low<=high:
            mid=(low+high)//2

            RowMaxIndex=self.findMaxIndex(mat,n,m,mid)

            left=mat[RowMaxIndex][mid-1]if mid>0 else -1
            right=mat[RowMaxIndex][mid+1] if mid <m-1 else -1

            if mat[ RowMaxIndex][mid]>left and mat[ RowMaxIndex][mid]>right:
                return [ RowMaxIndex,mid]
            elif mat[ RowMaxIndex][mid]<left:
                high=mid-1
            else:
                low=mid+1
        return [-1,-1]


    def findMaxIndex(self,mat,n,m,col):
        max_value=-1
        index=-1
        for i in range (n):
            if mat[i][col]>max_value:
                max_value=mat[i][col]
                index=i
        return index
    
        
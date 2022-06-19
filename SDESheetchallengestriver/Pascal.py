class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        a=[]
        for i in range(rowIndex+1):
            b=[]
            for j in range(i+1):
                if j==0 or j==i:
                    b.append(1)
                else:
                    b.append(a[i-1][j-1]+a[i-1][j])
                    
            a.append(b)
        return a[rowIndex]
      
https://leetcode.com/problems/pascals-triangle/

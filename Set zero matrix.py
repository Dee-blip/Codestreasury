Given an ‘N’ x ‘M’ integer matrix, if an element is 0, set its entire row and column to 0's, and return the matrix. In particular, your task is to modify it in such a way that if a cell has a value 0 (matrix[i][j] == 0), then all the cells of the ith row and jth column should be changed to 0.
You must do it in place.

def setZeros(matrix: List[List[int]]) -> None:
    row=len(matrix)
    col=len(matrix[0])
    
    r,c=set(),set()
    
    for i in range(row):
        for j in range(col):
            if matrix[i][j]==0:
                r.add(i)
                c.add(j)
                
    for i in range(row):
        for j in range(col):
            if i in r or j in c:
                matrix[i][j]=0
                
    return matrix
  
# https://www.codingninjas.com/codestudio/problems/set-matrix-zeros_3846774?topList=striver-sde-sheet-problems&leftPanelTab=0
    

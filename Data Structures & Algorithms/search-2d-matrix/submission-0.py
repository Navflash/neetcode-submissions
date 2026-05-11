class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix),len(matrix[0])

        i,j = 0,cols-1
        while i >= 0 and i < rows and j >= 0 and j < cols:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j-=1
            elif matrix[i][j] < target:
                i+=1

        return False
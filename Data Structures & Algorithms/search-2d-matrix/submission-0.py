class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        s = set()
        for i in range(rows):
            for j in range(cols):
                s.add(matrix[i][j])
        if target in s:
            return True
        else:
            return False

        # l,r = 0,rows*cols-1

        # while l<=r:
        #     m = (l+r)//2
        #     i,j = m//cols,m%cols
        #     if matrix[i][j] <target:
        #         l = m+1
        #     elif matrix[i][j] >target:
        #         r = m-1
        #     else:
        #         return True
        # return False
        
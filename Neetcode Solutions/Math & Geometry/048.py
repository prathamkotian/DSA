# Rotate 2D image by 90 degrees

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)

        # transpose the matrix
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        # reverse the rows of matrix
        for i in range(n):
            matrix[i].reverse()

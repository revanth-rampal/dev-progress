class Solution:
    def setMatrixZeroes(self, mat):
        copy=[k[:] for k in mat]
        for k in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[k][j]== 0: 
                    for i in range(len(mat)):
                        copy[i][j]=0 
                    for i in range(len(mat[0])):
                        copy[k][i]=0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j]=copy[i][j]

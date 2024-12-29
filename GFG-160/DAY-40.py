class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchMatrix(self, mat, x): 
    	# code here 
    	for i in range(len(mat)):
    	    for j in range(len(mat[0])):
    	        if mat [i][j]==x:
    	            return 'true' 
    	return False

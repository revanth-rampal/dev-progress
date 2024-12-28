
class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchRowMatrix(self, mat, x): 
    	# code here 
    	 for i in mat :
    	     if x in i :
    	         return True 
    	 return False 
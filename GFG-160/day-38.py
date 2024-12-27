class Solution:
	def matSearch(self, mat, x):
		# Complete this functio
		n= len(mat)
		m= len(mat[0])
		i=0
		k=m-1
		while i<n and k>=0:
		    if mat[i][k]==x:
		        return True
		    elif mat[i][k]>x:
		        k-=1
		    else:
		        i+=1
		return False
		

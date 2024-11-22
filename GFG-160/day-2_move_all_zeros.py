#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
	    n=len(arr)
        j=0
        for i in range(n):
	        if arr[i] !=0:
	            arr[j], arr[i] =arr[i],arr[j]
	            j+=1
	            
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends
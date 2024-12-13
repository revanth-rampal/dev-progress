class Solution:
	def mergeOverlap(self, arr):
		#Code here
		merge =[]
		arr.sort(key=lambda x:x[0])
		for i in arr:
		    if not merge or merge[-1][1]<i[0]:
		        merge.append(i)
		    else:
		            merge[-1][1]=max(merge[-1][1],i[1])
	    return merge


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        # a = list(map(int, input().strip().split()))
        arr = []
        # j = 0
        for i in range(n):
            a = list(map(int, input().strip().split()))
            x = a[0]
            # j += 1
            y = a[1]
            # j += 1
            arr.append([x, y])
        obj = Solution()
        ans = obj.mergeOverlap(arr)
        for i in ans:
            for j in i:
                print(j, end=" ")
        print()

# } Driver Code Ends
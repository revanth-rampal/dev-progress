#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        arr.sort()
        n = len(arr)
        if n <= 1:
            return 0
        result = arr[-1] - arr[0]
        for i in range(1, n):
            if arr[i] - k >= 0:
                min_height = min(arr[0] + k, arr[i] - k)
                max_height = max(arr[i - 1] + k, arr[-1] - k)
                result = min(result, max_height - min_height)
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, k)
        print(ans)
        tc -= 1

# } Driver Code Ends
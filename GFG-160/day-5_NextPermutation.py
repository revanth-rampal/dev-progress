#User function Template for python3

class Solution:
    def nextPermutation(self, arr):
        n = len(arr)
        pivot = next((i for i in range(n - 2, -1, -1) if arr[i] < arr[i + 1]), -1)

        if pivot == -1:
            arr.reverse()
            return arr

        swap = next(i for i in range(n - 1, pivot, -1) if arr[i] > arr[pivot])
        arr[pivot], arr[swap] = arr[swap], arr[pivot]
        arr[pivot + 1:] = reversed(arr[pivot + 1:])
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for i in range(N):
            arr[i] = int(arr[i])

        ob = Solution()
        ob.nextPermutation(arr)
        for i in range(N):
            print(arr[i], end=" ")
        print()

# } Driver Code Ends
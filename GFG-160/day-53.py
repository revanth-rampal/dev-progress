#User function Template for python3
class Solution:
    def sumClosest(self, arr, target):
        # code here
        n=len(arr)
        arr.sort()
        res=[]
        minDiff=float('inf')
        left=0
        right=n-1
        while left<right:
            curr=arr[left]+arr[right]
            if abs(target-curr)<minDiff:
                minDiff=abs(target-curr)
                res=[arr[left],arr[right]]
            if curr<target:
                left+=1
            elif curr>target:
                right-=1
            else:
                return res 
        return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends
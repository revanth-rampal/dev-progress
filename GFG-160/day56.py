#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        left =0
        right=0
        res=[]
        curr=0
        for i in range (len(arr)):
            curr+=arr[i]
            
            if curr>=target:
                right =i
                
            while curr > target and left < right :
                curr -= arr[left]
                left +=1
            if curr== target:
                res.append(left+1)
                res.append(right+1)
                return res
        return[-1]

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subarraySum(arr, d)
        print(" ".join(map(str, result)))
        tc -= 1
        print("~")

# } Driver Code Ends
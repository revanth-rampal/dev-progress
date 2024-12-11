#User function Template for python3
class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        #code here
        citations.sort(reverse=True)
        
        idx=0
        for i in range(len(citations)):
            if citations[i]>=i+1:
                idx=i+1
            else:
                break
        return idx


#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.hIndex(arr)

        print(result)
        print("~")

# } Driver Code Ends
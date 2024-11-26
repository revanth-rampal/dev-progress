from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        n: int = len(prices)
        profit: int =0 
        
        for i in range(1,n):
            if prices[i] > prices [i-1]:
                profit += prices[i] - prices[i-1]
        return profit


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.maximumProfit(arr)
        print(res)

# } Driver Code Ends
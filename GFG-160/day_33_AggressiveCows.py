#User function Template for python3


class Solution:

    def aggressiveCows(self, stalls, k):
        stalls.sort()

        def canPlace(d):
            count, last_pos = 1, stalls[0]
            for stall in stalls[1:]:
                if stall - last_pos >= d:
                    count += 1
                    last_pos = stall
                    if count == k:
                        return True
            return False

        left, right, result = 0, stalls[-1] - stalls[0], 0
        while left <= right:
            mid = (left + right) // 2
            if canPlace(mid):
                result, left = mid, mid + 1
            else:
                right = mid - 1
        return result
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.aggressiveCows(A, D)
        print(ans)
        print("~")
# } Driver Code Ends
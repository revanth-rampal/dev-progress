class Solution:
    def minChar(self, s):
        #Write your code here
        concat = s + '#' + s[::-1]
        n = len(concat)
        lps = [0] * n
        length = 0 
        
        for i in range(1, n):
            while length > 0 and concat[i] != concat[length]:
                length = lps[length - 1]
            if concat[i] == concat[length]:
                length += 1
            lps[i] = length
            
        return len(s) - lps[-1]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        obj = Solution()
        ans = obj.minChar(s)
        print(ans)
        print("~")

# } Driver Code Ends
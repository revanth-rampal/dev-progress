#User function Template for python3

class Solution:
    def search(self, pat, txt):
        # code here
        result =[]
        patlen = len(pat)
        txtlen= len(txt)
        for i in range(txtlen-patlen+1):
            if txt[i:i +patlen] == pat:
                result.append(i)
        return result
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans) == 0:
            print("[]", end="")
        for value in ans:
            print(value, end=' ')
        print()

# } Driver Code Ends
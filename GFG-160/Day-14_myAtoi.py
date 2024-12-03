#User function template for Python
class Solution:
    def myAtoi(self, s):
        # Code here
        s = s.lstrip()
        sign = -1 if s and s[0] == '-' else 1
        s = s[1:] if s and s[0] in '+-' else s
        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            else:
                break
        num *= sign
        return max(min(num, 2**31 - 1), -2**31)


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.myAtoi(s))
        print("~")

# } Driver Code Ends
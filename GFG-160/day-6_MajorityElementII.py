class Solution:
    # Function to find the majority elements in the array11
    def findMajority(self, arr):
        #Your Code goes here.
        n = len(arr)
        hmap = {}
        lst = []

        for num in arr:
            hmap[num] = hmap.get(num, 0) + 1

        one_third = n // 3
        for key, val in hmap.items():
            if val > one_third:
                lst.append(key)

        if len(lst) == 2 and lst[0] > lst[1]:
            lst[0], lst[1] = lst[1], lst[0]
        
        return lst 

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends
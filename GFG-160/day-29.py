#User function Template for python3

class Solution:
    def findMin(self, arr):
        #complete the function here
        l,r=0,len(arr)-1
        while l<r:
            mid=(l+r)//2
            if arr[mid]>arr[r]:
                l=mid+1
            else:
                r=mid
        return arr[l]


#{ 
 # Driver Code Starts
def main():
    T = int(input())

    while T > 0:
        a = list(map(
            int,
            input().strip().split()))  # Convert input to list of integers
        print(Solution().findMin(a))  # Call findMin with the array 'a'
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
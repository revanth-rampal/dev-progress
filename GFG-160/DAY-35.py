class Solution:
    def kthMissing(self, arr, k):
        # code here
        low,high=0,len(arr)-1
        while low<=high:
            mid =low +(high-low)//2
            miss=arr[mid]-(mid+1)
            if miss<k:
                low =mid+1
            else:
                high=mid-1
        return low+k 
        

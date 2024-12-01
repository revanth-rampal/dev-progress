#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    def kadane(nums):
        curr_sum = max_sum = nums[0]
        for num in nums[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
        return max_sum

    max_kadane = kadane(arr)
    total_sum = sum(arr)
    min_subarray = kadane([-num for num in arr])
    max_circular = total_sum + min_subarray

    return max(max_kadane, max_circular) if max_circular != 0 else max_kadane


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__ == "__main__":
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr))

        T -= 1

# } Driver Code Ends
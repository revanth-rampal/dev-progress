class Solution:
    def countSubarrays(self, arr, k):
        # code here
        sum_count={0:1}
        sum=0
        count=0
        for num in arr:
            sum+=num
            if sum -k in sum_count:
                count+=sum_count[sum-k]
            if sum in sum_count:
                sum_count[sum]+=1
            else:
                sum_count[sum]=1
        return count

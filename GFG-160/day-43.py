class Solution:
    #Complete the below function
    def countPairs(self,arr, target):
        #Your code here
        freq={}
        pair=0
        
        for num in arr:
            comp = target-num 
            if comp in freq:
                pair+=freq[comp]
                
            freq[num]=freq.get(num,0)+1
        return pair 
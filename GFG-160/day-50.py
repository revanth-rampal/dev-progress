class Solution:
    def subarrayXor(self, arr, k):
        # code here
        c=0
        xor=0
        feq={0:1}
        for num in arr:
            xor ^= num
            req= xor^k
            c+=feq.get(req,0)
            feq[xor]=feq.get(xor,0)+1
        return c
        


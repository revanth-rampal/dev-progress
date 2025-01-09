class Solution:
    def countTriplets(self, arr, target):
        # code here
        s1={}
        s2={}
        ret=0
        for ve in arr:
            ret+=s2.get(target-ve,0)
            for v in s1:
                s2[v+ve]=s2.get(v+ve,0)+s1.get(v,0)
            s1[ve]=s1.get(ve,0)+1
        return ret 
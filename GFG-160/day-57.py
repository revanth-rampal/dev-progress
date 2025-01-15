class Solution:
    def countDistinct(self, arr, k):
        # Code here
        a={}
        b=[]
        for i in range(k):
            a[arr[i]]=a.get(arr[i],0)+1
        b.append(len(a))
        for i in range(k,len(arr)):
            o=arr[i-k]
            a[o]-=1
            if a[o]==0:
                del a[o]
            c=arr[i]
            a[c]=a.get(c,0)+1
            b.append(len(a))
        return b 
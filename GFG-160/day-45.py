class Solution:
    def intersectionWithDuplicates(self, a, b):
        # code here
        a=set(a)
        b=set(b)
        result=a.intersection(b)
        return list(result)

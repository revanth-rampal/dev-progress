
class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        # code here
        return len(set(a+b))



class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        index={}
        start=0
        max_len = 0
        for i in range(len(s)):
            if s[i] in index and index[s[i]]>=start:
                start =index[s[i]]+1
            index[s[i]]=i
            max_len=max(max_len,i-start+1)
        return max_len 

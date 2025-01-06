class Solution:

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        r=[]
        d={}
        for i in arr:
            s=''.join(sorted(i))
            if s not in d :
                d[s]=len(r)
                r.append([])
            r[d[s]].append(i)
        return r
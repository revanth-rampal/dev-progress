class Solution:
    def findPages(self, arr, k):
        if k > len(arr): return -1
        def valid(mid): 
            students, pages = 1, 0
            for book in arr:
                if pages + book > mid: students, pages = students + 1, book
                else: pages += book
                if students > k: return False
            return True
        low, high = max(arr), sum(arr)
        while low <= high:
            mid = (low + high) // 2
            if valid(mid): high = mid - 1
            else: low = mid + 1
        return low

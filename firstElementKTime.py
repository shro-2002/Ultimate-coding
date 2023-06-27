# Given an array of N integers. Find the first element that occurs at least K number of times.

from collections import defaultdict

class Solution:
    def firstElementKTime(self,  arr, n, k):
        v = defaultdict(int)
        for i in range(n):
            v[arr[i]] += 1
            if v[arr[i]] >= k:
                return arr[i]
        return -1
    
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().strip().split())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.firstElementKTime(arr, n, k))

# } Driver Code Ends



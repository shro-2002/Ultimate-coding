# Given an array arr[] of positive integers of size N. Reverse every sub-array group of size K.

# Input:
# The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow.
# Each test case consist of two lines of input. The first line of each test case consists of an integer N(size of array)
# and an integer K separated by a space. The second line of each test case contains N space separated integers denoting
# the array elements.

# Output:
# For each test case, print the modified array.

# Given an array arr[] of positive integers of size N. Reverse every sub-array group of size K.

# Note: If at any instance, there are no more subarrays of size greater than or equal to K, then reverse the last subarray (irrespective of its size). You shouldn't return any array, modify the given array in-place.

class Solution:
    def reverseArray(self, arr, n, k):
        # code here
        i = 0
        while i < n:
            left = i
            right = min(i + k - 1, n - 1)
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            i += k
        return arr
    
    
    

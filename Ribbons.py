# You are given an array of integers a, where each element a[i] represents the length of a ribbon.Your goal is to obtain k ribbons of the same length, by cutting the ribbons into as many pieces as you want.
# Your task is to calculate the maximum integer length L for which it is possible to obtain at least k ribbons of length L by cutting the given ones.

# Example
# For a = [5, 2, 7, 4, 9] and k = 5, the output should be solution(a, k) = 4.

# Solution:

def solution(a, k):
    left, right = 0, max(a)
    while left < right:
        mid = (left + right + 1) >> 1
        cnt = sum(x // mid for x in a)
        if cnt >= k:
            left = mid
        else:
            right = mid - 1
    return left



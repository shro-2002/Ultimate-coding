# Given an array of integers a, your task is to calculate the digits that occur the most number of times in the array. Return the array of these digits in ascending order.

# Example
# For a = [25, 2, 3, 57, 38, 41], the output should be solution(a) = [2, 3, 5].
# Here are the number of times each digit appears in the array:
# 0 -> 0
# 1 -> 1
# 2 -> 2
# 3 -> 2
# 4 -> 1
# 5 -> 2
# 6 -> 0
# 7 -> 1
# 8 -> 1
# The most number of times any number occurs in the array is 2, and the digits which appear 2 times are 2, 3 and 5. So the answer is [2, 3, 5].

def solution(a):

    freq = [0] * 10
    for num in a:
        while num > 0:
            rem = num % 10
            num //= 10
            freq[rem] += 1
    maxi = max(freq)
    ans = []
    for i in range(10):
        if freq[i] == maxi:
            ans.append(i)
        
    return ans

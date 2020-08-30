# Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

# Example 1:

# Input: 5
# Output: 2
# Explanation: 5 = 5 = 2 + 3
# Example 2:

# Input: 9
# Output: 3
# Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
# Example 3:

# Input: 15
# Output: 4
# Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
# Note: 1 <= N <= 10 ^ 9.

class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        kmax = int(math.sqrt(2*N+0.25) - 0.5)
        output = 0
        for i in range(kmax):
            x = N/(i+1) - (i+2)/2
            if x.is_integer():
                output += 1
        return output

#Find Divisors / Integer Factorization Problem
#https://leetcode.com/problems/consecutive-numbers-sum/solution/
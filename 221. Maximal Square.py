# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

# Example:

# Input: 

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0

# Output: 4

import numpy as np
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:  
        matrix = np.array(matrix)
        area = 0
        if matrix != []:
            for edge in list(range(min(len(matrix),len(matrix[0])))):
                for i in range(len(matrix)-edge):
                    for j in range(len(matrix[0])-edge):
                        if '0' not in matrix[i:i+edge+1, j:j+edge+1]:
                            area = (edge+1)*(edge+1)
                if area != (edge+1)*(edge+1):
                    break
        return area

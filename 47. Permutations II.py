# Given a collection of numbers that might contain duplicates, return all possible unique permutations.

# Example:

# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used = [False for _ in range(len(nums))]
        def backtrack(path, used, depth, output):
            if depth == len(nums):
                #deepcopy以防出现问题
                newpath = copy.deepcopy(path)
                if newpath not in output:
                    output.append(newpath)       
            for i in range(len(nums)):
                if not used[i]:
                    #进行操作
                    path.append(nums[i])
                    #改变状态
                    used[i] = True
                    #下一层
                    backtrack(path, used, depth+1, output)
                    #重置状态
                    used[i] = False
                    path.pop()
        path = []
        depth = 0
        output = []  
        backtrack(path, used, depth, output)
        return output
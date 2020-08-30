# Given a collection of distinct integers, return all possible permutations.

# Example:

# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        def backtrack(depth = 0):
            #复制一个新数组
            new = nums
            #遍历到n层时结束一次选择
            if depth == n:  
                output.append(new[:])
            for i in range(depth, n):
                #选择这一层的第一个到最后一个
                new[depth], new[i] = nums[i], nums[depth]
                #遍历下一层
                backtrack(depth + 1)
                #重置这一层
                new[depth], new[i] = nums[i], nums[depth]
        backtrack()
        return output


# 回溯(backtrack)算法：
# 问题可以看成用不同的顺序选择数字到一个新的list中
# 每进行n次选择之后就完成了一次任务
# 然后可以依次返回上一步进行不同的选择
# 这里用first来代表进行了几次选择，也就是遍历深度depth
# 当depth=n时可以作为一种排列放入结果中
# 对于所有层进行遍历，也就是一个对树剪枝的过程

#另一种写法：
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False for _ in range(len(nums))]
        def backtrack(path, used, depth, output):
            if depth == len(nums):
                #deepcopy以防出现问题
                output.append(copy.deepcopy(path))
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


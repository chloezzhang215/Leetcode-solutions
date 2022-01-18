##迭代法
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res += [[i] + num for num in res]
        return res
      
##回溯法

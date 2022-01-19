class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        res = []
        nums.sort()

        def backtracking(index, tmp):
            if tmp not in res:
                res.append(tmp)
            for i in range(index,len(nums)):
                backtracking(i+1, tmp+[nums[i]])
        
        backtracking(0,[])
        return res

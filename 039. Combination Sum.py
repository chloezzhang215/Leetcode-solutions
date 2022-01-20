class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        if min(candidates) > target:
            return []

        res = []
        candidates.sort()

        def backtracking(candidates,target,tmp):
            if target == 0:
                res.append(tmp)
            if target < 0:
                return
            for i in range(len(candidates)):
                if candidates[i] > target:
                    break
                backtracking(candidates[i:], target - candidates[i], tmp + [candidates[i]])
        backtracking(candidates,target,[])
        return res

        

            

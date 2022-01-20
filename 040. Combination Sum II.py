class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        
        res = []
        candidates.sort()

        def backtracking(index,sum,tmp):
            if sum == target:
                res.append(tmp)
                return
            for i in range(index,len(candidates)):
                if sum + candidates[i] > target:
                    break
                if i > index and candidates[i]==candidates[i-1]:
                    continue
                backtracking(i+1,sum+candidates[i],tmp+[candidates[i]])
        
        backtracking(0,0,[])
        return res
        

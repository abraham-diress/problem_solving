class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        tmp = []
        
        def backtrack(i, remaining):
            if remaining == 0:
                ans.append(tmp.copy())
            
            if remaining < 0:
                return 
            
            for j in range(i, len(candidates)):
                tmp.append(candidates[j])
                backtrack(j, remaining - candidates[j])
                tmp.pop()
        
        backtrack(0, target)
        return ans

        

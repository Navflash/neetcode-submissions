class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        curr = []
        res = []

        def combination(index,sumleft,candidates,curr,res):
            if sumleft == 0:
                res.append(list(curr))
                return

            if index >= len(candidates) or sumleft < 0:
                return


            curr.append(candidates[index])
            combination(index+1,sumleft-candidates[index],candidates,curr,res)
            curr.pop()

            next_index = index+1
            while next_index < len(candidates) and candidates[next_index]==candidates[index]:
                next_index+=1
            combination(next_index,sumleft,candidates,curr,res)

        combination(0,target,candidates,curr,res)
        return res
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        cur = []
        res = []

        def makecombination(i,nums,remSum,cur,res):
            if remSum == 0:
                res.append(list(cur))
                return

            if remSum < 0 or i >= len(nums):
                return

            cur.append(nums[i])

            makecombination(i,nums,remSum-nums[i],cur,res)

            cur.pop()

            makecombination(i+1,nums,remSum,cur,res)

        makecombination(0,nums,target,cur,res)
        return res
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        curr= []
        res = []


        def subset(index,nums,curr,res):

            if index >= len(nums):
                res.append(list(curr))
                return

            curr.append(nums[index])
            subset(index+1,nums,curr,res)
            curr.pop()

            next_index = index+1
            while next_index < len(nums) and nums[next_index] == nums[index]:
                next_index+=1

            subset(next_index,nums,curr,res)

        subset(0,nums,curr,res)
        return res
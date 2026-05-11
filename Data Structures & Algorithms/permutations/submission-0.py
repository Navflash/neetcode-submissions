class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def per(index,nums,res):
            if index == len(nums):
                res.append(nums[:])
                return

            for i in range(index,len(nums)):
                nums[index],nums[i] = nums[i],nums[index]
                per(index+1,nums,res)
                nums[index],nums[i] = nums[i],nums[index]

        per(0,nums,res)
        return res

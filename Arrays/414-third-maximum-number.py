class Solution(object):
    def thirdMax(self, nums):
        unique_nums=sorted(set(nums),reverse=True)
        if len(unique_nums)>=3:
            return unique_nums[2]
        return unique_nums[0]

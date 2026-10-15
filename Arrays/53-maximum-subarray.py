class Solution(object):
    def maxSubArray(self, nums):
        l_sum=0
        result=[]
        for num in nums:
            l_sum=max(num,l_sum+num) 
            result.append(l_sum)
        return max(result)

class Solution(object):
    def runningSum(self, nums):
        result = 0
        answer = []

        for num in nums:
            result += num
            answer.append(result)

        return answer

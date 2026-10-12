class Solution(object):
    def majorityElement(self, nums):
        answer = {}

        for num in nums:
            answer[num] = answer.get(num, 0) + 1

        for num in answer:
            if answer[num] > len(nums) // 2:
                return num

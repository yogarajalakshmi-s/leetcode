# https://leetcode.com/problems/product-of-array-except-self/description/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0 for i in range(len(nums))]
        left = 1
        right = 1

        for i in range(len(nums)):
            print(i)
            answer[i] = left
            left *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer

# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        ptr = 0

        while ptr <= right:
            if nums[ptr] == 0:
                nums[left], nums[ptr] = nums[ptr], nums[left]
                left += 1
                ptr += 1
            elif nums[ptr] == 2:
                nums[right], nums[ptr] = nums[ptr], nums[right]
                right -= 1
            else:
                ptr += 1

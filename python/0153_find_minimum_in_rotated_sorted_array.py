from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            pivot_index = (left + right) // 2

            if nums[pivot_index] >= nums[left]:
                left = pivot_index + 1
            else:
                right = pivot_index

        return nums[left]

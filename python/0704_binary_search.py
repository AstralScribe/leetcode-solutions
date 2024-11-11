from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            pivot_index = left + (right - left) // 2
            pivot = nums[pivot_index]

            if pivot == target:
                return pivot_index

            if pivot > target:
                right = pivot_index
            else:
                left = pivot_index + 1

        return -1


def test_solution():
    s = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    assert s.search(nums, target) == 4


def test_solution2():
    s = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    assert s.search(nums, target) == -1

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        trapped_water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                trapped_water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                trapped_water += right_max - height[right]

        return trapped_water


s = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
assert s.trap(height) == 6


def test_solution():
    s = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    assert s.trap(height) == 6


def test_solution2():
    s = Solution()
    height = [4, 2, 0, 3, 2, 5]
    assert s.trap(height) == 9


def test_solution3():
    s = Solution()
    height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
    assert s.trap(height) == 9

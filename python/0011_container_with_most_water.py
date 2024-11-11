from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left, right = 0, len(height) - 1
        max_height = max(height)
        while left < right:
            if (right - left) * max_height < area:
                break
            area = max(area, (right - left) * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return area


def test_solution():
    s = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert s.maxArea(height) == 49


def test_solution2():
    s = Solution()
    height = [1, 1]
    assert s.maxArea(height) == 1


def test_solution3():
    s = Solution()
    height = [1, 7, 2, 5, 4, 7, 3, 6]

    assert s.maxArea(height) == 36

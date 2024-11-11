from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        left, right = 0, row * col

        while left < right:
            pivot_index = (left + right) // 2

            i = pivot_index // col
            j = pivot_index % col
            val = matrix[i][j]

            if target == val:
                return True
            if target > val:
                left = pivot_index + 1
            else:
                right = pivot_index

        return False


def test_solution():
    s = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert s.searchMatrix(matrix, 13) is False


def test_solution2():
    s = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert s.searchMatrix(matrix, 16) is True

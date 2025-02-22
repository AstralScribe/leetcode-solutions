from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        prev = nums[-1]
        position = -1

        lex_check = False

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < prev:
                position = i
                lex_check = False
                break
            else:
                lex_check = True

        if lex_check:
            nums.sort()
        else:
            small_val = nums[position + 1]
            idx_sv = position + 1

            for i in range(position + 1, len(nums)):
                if nums[i] < small_val:
                    small_val = nums[i]
                    idx_sv = i

            temp = nums[position]
            nums[position] = nums[idx_sv]
            nums[idx_sv] = temp

            temp_array = nums[position + 1 :]
            temp_array.sort()
            nums = nums[:position] + temp_array


s = Solution()
# nums = [1, 2, 4, 3, 7, 6, 5]
nums = [1, 2]
s.nextPermutation(nums)


def test_solution1():
    s = Solution()
    nums = [1, 2, 3]
    output = [1, 3, 2]
    s.nextPermutation(nums)
    assert nums == output


def test_solution2():
    s = Solution()
    nums = [1, 2, 4, 3, 7, 6, 5]
    # output = [1,2,4,7,3,5,6]
    output = [1, 2, 4, 5, 3, 6, 7]
    s.nextPermutation(nums)
    assert nums == output

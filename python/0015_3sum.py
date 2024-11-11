from typing import Counter, List
from bisect import bisect_right


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return []

        nums.sort()
        output = []

        for index, value in enumerate(nums):
            if value > 0:
                break

            if index > 0 and value == nums[index - 1]:
                continue

            tail = index + 1
            head = len(nums) - 1

            while head > tail:
                sum = value + nums[tail] + nums[head]
                if sum == 0:
                    output.append([value, nums[tail], nums[head]])
                    head -= 1
                    tail += 1
                    while nums[tail] == nums[tail - 1] and head > tail:
                        tail += 1
                    continue

                if sum > 0:
                    head -= 1
                elif sum < 0:
                    tail += 1

        return output

    # Fastest solution on leetcode
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        index = 1
        x = nums[0]
        counter = 1
        while index < len(nums):
            if nums[index] == x:
                counter = counter + 1
                if x == 0:
                    if counter > 3:
                        nums.pop(index)
                    else:
                        index = index + 1
                elif counter > 2:
                    nums.pop(index)
                else:
                    index = index + 1
            else:
                x = nums[index]
                counter = 1
                index = index + 1
        if not all(n > 0 for n in nums):
            counts = Counter(nums)
            result = [[0, 0, 0]] if counts[0] >= 3 else []
            nums = [i for i in sorted(counts) if i != 0]
            if counts[0] > 0:
                for i in nums:
                    if i > 0:
                        break
                    if -i in counts:
                        result.append([-i, 0, i])
            for i in nums:
                if i & 1:
                    continue
                remaining = -i >> 1
                if counts[remaining] >= 2:
                    result.append([i, remaining, remaining])
            for i, n in enumerate(nums):
                kk = -(nums[0] + n)
                if kk < n:
                    break
                j = bisect_right(nums, -n << 1) if n < 0 else i + 1
                k = bisect_right(nums, kk)
                for right in nums[j:k]:
                    left = -(n + right)
                    if left in counts:
                        result.append([left, n, right])
            del counts, nums
            return result
        else:
            return []


def test_solution():
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    assert s.threeSum(nums) == [[-1, -1, 2], [-1, 0, 1]]
    assert s.threeSum2(nums) == [[-1, -1, 2], [-1, 0, 1]]


def test_solution2():
    s = Solution()
    nums = [0, 1, 1]
    assert s.threeSum(nums) == []
    assert s.threeSum2(nums) == []


def test_solution3():
    s = Solution()
    nums = [0, 0, 0]
    assert s.threeSum(nums) == [[0, 0, 0]]
    assert s.threeSum2(nums) == [[0, 0, 0]]

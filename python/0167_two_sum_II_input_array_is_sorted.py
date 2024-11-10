from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while (l<r):
            current_sum = numbers[l] + numbers[r]
            if  current_sum == target:
                return [l+1,r+1]
            if current_sum < target:
                l+=1
            if current_sum > target:
                r-=1
        return []
        




s = Solution()

def test_solution1():
    numbers = [2,7,11,15]
    target = 9
    assert s.twoSum(numbers, target) == [1,2]

def test_solution2():
    numbers = [2,3,4]
    target = 6
    assert s.twoSum(numbers, target) == [1,3]

def test_solution3():
    numbers = [-1,0]
    target = -1
    assert s.twoSum(numbers, target) == [1,2]


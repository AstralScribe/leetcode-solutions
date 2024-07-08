from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        for i, num in enumerate(nums):
            if target - num in seen:
                return [nums.index(target - num), i]
            seen.add(num)
        return []

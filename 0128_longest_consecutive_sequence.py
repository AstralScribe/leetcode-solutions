from typing import List

# Solution #1

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mapper = {}
        max_length = 0

        for num in nums:
            if num in mapper.keys():
                continue
            mapper[num] = 0
            num_left = mapper.get(num-1, 0)
            num_right = mapper.get(num+1, 0)
            count = num_left+num_right+1
            mapper[num-num_left] = count
            mapper[num+num_right] = count
            print(mapper)
            max_length = max(max_length, count)
        
        return max_length
    
def run_test(nums):
    s = Solution()
    val = s.longestConsecutive(nums)
    return val

if __name__ == "__main__":
    nums = [0,3,7,2,5,8,4,6,0,1]
    val = run_test(nums)
    print(val)

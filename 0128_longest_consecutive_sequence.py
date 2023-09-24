from typing import List

# Solution #1

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mapper = {}
        max_length = 0

        for i in nums:
            if i in mapper.keys():
                continue
            mapper[i] = [i,i]
            left_end = mapper[i-1][0] if mapper.get(i-1, False) else False
            right_end = mapper[i+1][1] if  mapper.get(i+1, False) else False
            if left_end:
                mapper[i][0] = left_end
                mapper[i-1][1] = 
            if right_end:
                mapper[i][1] = right_end
            print(mapper) 
            max_length = max(max_length, mapper[i][1]-mapper[i][0]+1)
        
        return max_length


def run_test(nums):
    s = Solution()
    val = s.longestConsecutive(nums)
    return val

if __name__ == "__main__":
    nums = [0,3,7,2,5,8,4,6,0,1]
    val = run_test(nums)
    print(val)

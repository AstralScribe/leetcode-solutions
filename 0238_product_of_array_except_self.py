class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        answer = [1]*size
        
        left = 1
        right = 1
        
        for i in range(size):
            answer[i] = answer[i] * left
            left = left * nums[i]
            
        for i in range(size-1,-1,-1):
            answer[i] = answer[i] * right
            right = right * nums[i]
            
        return answer

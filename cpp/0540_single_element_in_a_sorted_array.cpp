#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int singleNonDuplicate(vector<int>& nums) {
    int left = 0, right = nums.size() - 1;
    
    while (left <= right) {
      int mid = left + (right - left) / 2;
      
      if (nums[mid] != nums[mid + 1] && nums[mid] != nums[mid - 1]) {
        return nums[mid];
      }
      
      if (left+2 <= right && nums[left] == nums[left+1]) left+=2;
      if (nums[right] == nums[right+1]) right-=2;
      
    }
    return nums[left];
  }
};
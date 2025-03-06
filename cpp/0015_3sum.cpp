#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
  vector<vector<int>> threeSum(vector<int>& nums) {
    if (nums.size() == 0) return {{}};
    
    std::sort(nums.begin(), nums.end());
    vector<vector<int>> result;
    
    for (int i = 0; i < nums.size(); i++) {
      if (i > 0 && nums[i] == nums[i - 1]) {
        continue;
      }
      int left = i + 1, right = nums.size() - 1;
      while (left < right) {
        int sum = nums[i] + nums[left] + nums[right];
        if (sum == 0) {
          result.push_back({nums[i], nums[left], nums[right]});
          left++;
          right--;
          while (left < right && nums[left] == nums[left-1]) {
            left++;
          }
          while (right > left && nums[right] == nums[right+1]) {
            right--;
          }
          continue;
        }
        if (sum > 0) {
          right--;
        }
        if (sum < 0) {
          left++;
        }
      }
    }
    return result;
  }
};  
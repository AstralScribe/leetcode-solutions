#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void printMatrix(const vector<vector<int>> &matrix) {
  for (int i = 0; i < matrix.size(); ++i) {
    for (int j = 0; j < matrix[i].size(); ++j) {
      cout << matrix[i][j] << " ";
    }
    cout << endl;
  }
  cout << endl;
}

class Solution {
public:
  vector<vector<int>> fourSum(vector<int>& nums, int target) {
    if (nums.empty()) return vector<vector<int>>();
    sort(nums.begin(), nums.end());
    vector<vector<int>> ans;
    
    for (int i = 0; i < nums.size(); i++) {
      if (i > 0 && nums[i] == nums[i - 1]) continue;
      int new_target = target - nums[i];
      for (int j = i + 1; j < nums.size(); j++) {
        if (j > i + 1 && nums[j] == nums[j - 1]) continue; 
        int left = j+1, right = nums.size()-1;
        while (left < right) {
          int sum = nums[left] + nums[right] + nums[j];
          if (sum == new_target) {
            ans.push_back({nums[i], nums[j], nums[left], nums[right]});
            left++;
            right--;
            while (left < right && nums[left] == nums[left-1]) left++;
            while (right > left && nums[right] == nums[right+1]) right--;
            continue;
          }
          if (sum < new_target) left++;
          if (sum > new_target) right--;
        }
     }
    }
    return ans;
  }
};

int main() {
  vector<int> nums = {1,0,-1,0,-2,2};
  Solution s;
  vector<vector<int>> ans = s.fourSum(nums, 0);
  printMatrix(ans);
}
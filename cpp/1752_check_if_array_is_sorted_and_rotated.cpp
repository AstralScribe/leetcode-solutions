#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  bool check(vector<int>& nums) {
    if (checkSorted(nums, 0, nums.size())) return true;
    int rotation = findRotation(nums); 
    if (checkSorted(nums, 0, rotation) && checkSorted(nums, rotation + 1, nums.size()) && nums[0] >= nums[nums.size()-1]) {
      return true;
    }
    return false;
  }
  
  int findRotation(vector<int>& nums) {
    int n = nums.size();
    int min = 0;
    for (int i = 0; i < n; i++) {
      if (nums[i] <= nums[min]) {
        min = i;
      }
    }
    return min;
  }
  
  bool checkSorted(const vector<int>& nums, int left, int right) {
    for (int i = left; i < right; i++) {
      if (nums[i] < nums[i - 1]) {
        return false;
      }
    }
    return true;
  }
};

int main() {
  vector<int> nums = {6,10,6};
  Solution s;
  cout << s.check(nums) << endl;
}
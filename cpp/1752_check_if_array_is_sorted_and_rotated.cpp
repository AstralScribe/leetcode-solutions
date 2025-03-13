#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  bool check(vector<int> &nums) {
    auto array_size = nums.size();
    int b_rotation_idx = 0;
    bool b_rotation = false;
    for (auto i = 0; i < array_size - 1; i++) {
      if (nums[i] <= nums[i + 1] && !b_rotation)
        continue;
      if (!b_rotation) {
        b_rotation = true;
        if (nums[0] < nums[i + 1])
          return false;
        continue;
      }
      if (nums[0] >= nums[i + 1] && nums[i] <= nums[i + 1])
        continue;
      return false;
    }
    return true;
  }
};

int main() {
  vector<int> nums = {6, 10, 6};
  Solution s;
  cout << s.check(nums) << endl;
}
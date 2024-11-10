#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
 public:
  vector<int> twoSum(const vector<int>& nums, int target) {
    unordered_map<int, int> seen;
    vector<int> result;

    for (int i = 0; i < nums.size(); i++) {
      int comp = target - nums[i];
      if (seen.count(comp)) return {seen[comp], i};
      seen[nums[i]] = i;
    }
    return {};
  }
};

int main() {
  vector<int> nums{2, 7, 11, 15};
  int target = 9;

  Solution s;

  vector<int> result;
  result = s.twoSum(nums, target);
  for (auto& i : result) {
    cout << i << endl;
  }
}

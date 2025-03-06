#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> searchRange(vector<int> &nums, int target) {
    int low = 0, high = nums.size() - 1;

    while (low <= high) {
      int mid = low + (high - low) / 2;
      if (nums[mid] == target) {
        int lbound = mid, rbound = mid;
        while (nums[lbound] == target && lbound >= low) lbound--;
        while (nums[rbound] == target && rbound <= high) rbound++;
        lbound++;
        rbound--;
        return {lbound, rbound};
      } else if (nums[mid] < target) {
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }

    return {-1, -1};
  }
};

int main() {

  vector<int> nums = {5, 7, 7, 8, 8, 10};
  int target = 8;

  Solution s;
  vector<int> res = s.searchRange(nums, target);

  for (int i = 0; i < res.size(); i++) {
    cout << res[i] << " ";
  }
}

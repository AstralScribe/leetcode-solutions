#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  bool search(vector<int> &nums, int target) {
    int left = 0, right = nums.size() - 1;

    while (left <= right) {
      int mid = left + (right - left) / 2;

      if (nums[mid] == target || nums[left] == target || nums[right] == target) {
        return true;
      }

      if (nums[left] == nums[mid]) {
        while (left <= right && nums[left] == nums[mid])
          left++;
        left--;
      }
      if (nums[right] == nums[mid]) {
        while (left <= right && nums[right] == nums[mid])
          right--;
      }

      if (nums[left] < nums[mid]) {
        if (nums[left] <= target && target <= nums[mid - 1]) {
          right = mid - 1;
        } else {
          left = mid + 1;
        }
      } else {
        if (mid + 1 <= right && nums[mid + 1] <= target &&
            target <= nums[right]) {
          left = mid + 1;
        } else {
          right = mid - 1;
        }
      }
    }
    return false;
  }
};

int main() {
  vector<int> nums = {1, 0, 1, 1, 1};
  Solution s;
  cout << s.search(nums, 0) << endl;
}

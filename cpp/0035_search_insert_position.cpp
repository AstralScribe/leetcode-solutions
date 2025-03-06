#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int searchInsert(vector<int>& nums, int target) {
    int low = 0, high = nums.size(), mid = 0;
    if (target < nums[low]) return low;
    if (target > nums[high-1]) return high;

    while (low <= high) {
      mid = low + (high - low) / 2;
      if (nums[mid] == target)
        return mid;
      else if (nums[mid] < target)
        low = mid + 1;
      else
        high = mid - 1;
    }
    if (nums[mid] < target)
      return mid+1;
    return mid;
  }
};


int main() {
  vector<int> nums = {1,3,5,6};
  int target = 2;
  
  Solution s;
  cout << s.searchInsert(nums, target) << endl;
  return 0;
}
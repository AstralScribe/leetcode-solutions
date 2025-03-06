#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int maxProduct(vector<int> &nums) {
    int max = -100;
    int pd = 1;
    int n = nums.size();

    for (int i = 0; i < n; i++) {
      pd *= nums[i];
      max = max > pd ? max : pd;
      if (pd == 0)
        pd = 1;
    }
    pd = 1;

    for (int i = n - 1; i >= 0; i--) {
      pd *= nums[i];
      max = max > pd ? max : pd;
      if (pd == 0)
        pd = 1;
    }
    return max;
  }
};

int main() {
  // std::vector<int> nums{-5, -1, -3, -4, -2};
  // std::vector<int> nums{-5, 0};
  std::vector<int> nums{1, 2, 3, 4, -5, 0, -6, 7};
  Solution s;
  cout << s.maxProduct(nums) << endl;
}
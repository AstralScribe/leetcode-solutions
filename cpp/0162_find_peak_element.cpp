#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int findPeakElement(vector<int>& nums) {
    int left = 1, right = nums.size() - 1;

    if (nums[right-1] < nums[right]) return right;
    if (nums[left-1] > nums[left]) return 0;
    
    while (left < right) {
      if (nums[left-1] < nums[left] && nums[left+1] < nums[left]) {
        return left;
      }
      left++;
    }
  }
};


int main() {
  
  vector<int> nums = {1,2,1,3,5,6,4};
  Solution s;
  cout << s.findPeakElement(nums) << endl;
}
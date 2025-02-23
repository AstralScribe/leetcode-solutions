#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
  int subarraySum(vector<int>& nums, int k) {
    auto sum_total  = accumulate(nums.begin(), nums.end(), 0);
    if (sum_total == k)
      return 1;
    if (sum_total < k)
      return 0;
    
    int count = 0;

    
        
    
    return count;
  }
};


int main() {
  vector<int> nums{1,2,3,4,5,6,7,8,9};
  int k = 45;
  Solution s;
  cout << s.subarraySum(nums, k) << endl;
}
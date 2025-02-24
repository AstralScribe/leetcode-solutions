#include <iostream>
#include <numeric>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
  int subarraySum(vector<int> &nums, int k) {
    int count = 0;

    unordered_map<int, int> m;
    m.insert({0, 1});

    int sum_at_point = 0;

    for (int i = 0; i < nums.size(); ++i) {
      sum_at_point += nums[i];
      int remove = sum_at_point-k;
      count += m[remove];
      m[sum_at_point] += 1;
    }
    return count;
  }
};

int main() {
  vector<int> nums{-1, -1, 1};
  int k = 0;
  Solution s;
  cout << s.subarraySum(nums, k) << endl;
}
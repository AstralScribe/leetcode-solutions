#include <vector>

using namespace std;

class Solution {
 public:
  vector<int> twoSum(vector<int>& numbers, int target) {
    int l = 0;
    int r = numbers.size() - 1;
    int current_num;
    vector<int> result{};

    while (l < r) {
      current_num = numbers[l] + numbers[r];
      if (current_num == target) {
        // return {l + 1, r + 1};
        result.push_back(l + 1);
        result.push_back(r + 1);
        return result;
      }
      if (current_num < target) l++;
      if (current_num > target) r--;
    }

    return result;
  }
};

#include <iostream>
#include <vector>
#include <unordered_map>
#include <cmath>

using namespace std;

class Solution {
public:
  vector<int> majorityElement(vector<int>& nums) {
    vector<int> res;
    int floor_val = std::floor(float(nums.size())/3);
    
    unordered_map<int, int> map;
    
    for (int num : nums) {
      map[num]++;
    }
    
    for (auto &[key, val] : map) {
      if (val > floor_val) {
        res.push_back(key);
      }
    }
    
    return res; 
  }
};

int main() {
  vector<int> nums = {1,2};
  Solution s;
  vector<int> res = s.majorityElement(nums);
  for (int i = 0; i < res.size(); i++) {
    cout << res[i] << endl;
  }
}
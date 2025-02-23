#include <cassert>
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
 public:
  int longestConsecutive(vector<int>& nums) {
    int max_length{};

    unordered_map<int, int> hash_map{};

    for (auto& num : nums) {
      if (hash_map.find(num) != hash_map.end()) {
        continue;
      }
      hash_map[num] = 0;
      auto num_left =
          (hash_map.find(num - 1) != hash_map.end()) ? hash_map[num - 1] : 0;
      auto num_right =
          (hash_map.find(num + 1) != hash_map.end()) ? hash_map[num + 1] : 0;
      int count = num_right + num_left + 1;
      hash_map[num - num_left] = count;
      hash_map[num + num_right] = count;
      std::cout << num << " ";
      for (auto& i : hash_map) {
        std::cout << "{" << i.first << "," << i.second << "}, ";
      }
      std ::cout << std::endl;
      max_length = max(max_length, count);
    }

    return max_length;
  }
};

int main() {
  Solution s;
  std::vector<int> nums = {4,  0,  -4, -2, 2, 5, 2,  0, -8, -8, -8,
                           -8, -1, 7,  4,  5, 5, -4, 6, 6,  -3};

  auto out = s.longestConsecutive(nums);
  std::cout << out;
  // assert(out == 4);
}

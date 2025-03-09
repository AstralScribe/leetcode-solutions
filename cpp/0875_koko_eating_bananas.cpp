#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
  int TimeTaken (const vector<int>& nums, int k) {
    int out = 0;
    for (const auto& num : nums) {
      out += (num + k - 1) / k;
    }
    return out;
  }
  int minEatingSpeed(vector<int>& piles, int h) {
    int low = 1;
    int high = *max_element(piles.begin(), piles.end());

    while (low <= high) {
      int mid = low + (high-low) / 2;

      int tt = TimeTaken(piles, mid);
      if (tt == h) return mid;
      if (tt > h) low = mid + 1;
      else high = mid - 1;
    }
        
    return -1;
  }
};


int main() {
  vector<int> piles{3,6,7,11};
  int h = 8;
  Solution s;
  cout << s.minEatingSpeed(piles, h) << endl;
}
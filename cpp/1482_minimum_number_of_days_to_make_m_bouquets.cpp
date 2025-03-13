#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int bloomCount(vector<int> &bloomDay, int day, int flowers) {
    int count = 0;
    int num_flowers = 0;
    for (auto &bd : bloomDay) {
      if (bd <= day) {
        num_flowers++;
      } else {
        num_flowers = 0;
      }
      if (num_flowers != 0 && num_flowers % flowers == 0) {
        count++;
        num_flowers = 0;
      }
    }
    return count;
  }

  int minDays(vector<int> &bloomDay, int m, int k) {
    const int num_flowers = bloomDay.size();
    if (num_flowers < m * k)
      return -1;

    int low = *min_element(bloomDay.begin(), bloomDay.end());
    int high = *max_element(bloomDay.begin(), bloomDay.end());

    while (low <= high) {
      int mid = low + (high - low) / 2;

      int num_bouques = bloomCount(bloomDay, mid, k);
      // if (num_bouques == m)
      //    return mid;
      if (num_bouques < m) {
        low = mid+1;
      } else {
        high = mid-1;
      }
    }

    return low;
  }
};

int main() {
  Solution s;
  // vector<int> arr{12,7,7,7,10,4,8,7,7,6,12,12};
  vector<int> arr{7,7,7,7,12,7,7};
  int m = 2;
  int k = 3;

  std::cout << s.minDays(arr, m, k) << std::endl;
}


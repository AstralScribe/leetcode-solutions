#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int findKthPositive(vector<int> &arr, int k) {
    int size = arr.size();
    if (arr[size-1] == size) return size + k;
    int low = 0, high = size-1;

    while (low <= high) {
      int mid = low + (high - low) / 2;
      if (arr[mid] - (mid+1) < k) low = mid+1;
      else high = mid - 1;
    }
    
    return high + k + 1;
  }
};

int main() {
  vector arr{2, 3,4,7,11};
  int k = 5;

  Solution s;
  cout << s.findKthPositive(arr, k) << endl;
}
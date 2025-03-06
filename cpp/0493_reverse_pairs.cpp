#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int merge(vector<int> &arr, int low, int high) {
    int count = 0;
    if (low >= high) {
      return count;
    }
    int mid = low + (high - low) / 2;

    count += merge(arr, low, mid);
    count += merge(arr, mid + 1, high);

    vector<int> temp;
    int i = low, j = mid + 1 , k = mid+1;
    
    for (int x = i; x <= mid; x++) {
      while (k <= high && static_cast<long long>(arr[x]) >
                              2 * static_cast<long long>(arr[k])) {
        k++;
      }
      count += k - mid - 1;
    }

    while (i <= mid && j <= high) {
      if (arr[i] < arr[j]) {
        temp.push_back(arr[i]);
        i++;
      } else {
        temp.push_back(arr[j]);
        j++;
      }
    }

    while (i <= mid) {
      temp.push_back(arr[i]);
      i++;
    }
    while (j <= high) {
      temp.push_back(arr[j]);
      j++;
    }

    for (int k = low; k <= high; k++) {
      arr[k] = temp[k - low];
    }

    return count;
  }

  int reversePairs(vector<int> &arr) { return merge(arr, 0, arr.size() - 1); }
};
//{ Driver Code Starts.

int main() {
  // vector<int> a{1, 3, 2, 3, 1};
  vector<int> a{5, 4, 3, 2, 1};
  // vector a{-185,143,-154,-338};
  Solution obj;
  cout << obj.merge(a, 0, a.size() - 1) << endl;
}

// } D

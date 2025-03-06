#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    int i = m-1, j = n-1, k=1;
    while(i>=0){
      while(j>=0){
        if (i==-1) break;
        if (nums1[i] > nums2[j]) {
          nums1[m+n-k] = nums1[i];
          i--;
        } else {
          nums1[m+n-k] = nums2[j];
          j--;
        }
        k++;
      }
      if (j==-1) break;
    }
    while(i>=0){
      nums1[m+n-k] = nums1[i];
      i--;
      k++;
    }
    while(j>=0){
      nums1[m+n-k] = nums2[j];
      j--;
      k++;
    }
  }
};
int main() {
  vector<int> nums1 = {2,0};
  vector<int> nums2 = {1};
  Solution s;
  s.merge(nums1, 1, nums2, 1);
  for (auto i : nums1) {
    cout<<i<<" ";
  }
}
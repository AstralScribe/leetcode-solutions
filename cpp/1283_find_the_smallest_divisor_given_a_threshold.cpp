#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    int DivisorSum(vector<int>& nums, int divisor){
        int sum = 0;
        for(const auto& num: nums) sum += (num + divisor - 1) / divisor;
        return sum;
    }

    int smallestDivisor(vector<int>& nums, int threshold) {

        if (threshold > nums.size()) return -1;
        
        int low = 1;
        int high = *max_element(nums.begin(), nums.end());

        while (low <= high){
            int mid = low + (high - low) / 2;
            int divisor_sum = DivisorSum(nums, mid);
            if (divisor_sum > threshold) low = mid+1;
            else high = mid - 1;
        }

        return low;
    }
};

int main(){
  vector<int> array{44,22,33,11,1};
  Solution s;
  cout << s.smallestDivisor(array, 5) << endl;
}
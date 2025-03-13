#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int DaysNeeded(const vector<int>& weights, int capacity) {
        int num_days = 0;
        int curr_capacity = 0;
        for (const auto& weight : weights) {
            if (curr_capacity + weight > capacity) {
                num_days++;
                curr_capacity = 0;
            }
            curr_capacity += weight;
        }
        num_days++;
        return num_days;
    }

    int shipWithinDays(vector<int>& weights, int days) {
        long long low = *max_element(weights.begin(), weights.end());
        long long high = 0;

        for (const auto& weight: weights){
            high += weight;
        }


        while (low <= high) {
            long long mid = low + (high - low) / 2;
            int d_needed = DaysNeeded(weights, mid);
            if (d_needed <= days)
                // return (int) mid;
            // if (d_needed < days)
                high = mid-1;
            else
                low = mid + 1;
        }

        return int(low);
    }
};

int main(){
    vector<int> nums{1,2,3,1,1};
    int days = 4;
    Solution s;
    cout << s.shipWithinDays(nums, days);
}
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

void printMatrix(const vector<vector<int>> &matrix) {
  for (int i = 0; i < matrix.size(); ++i) {
    for (int j = 0; j < matrix[0].size(); ++j) {
      cout << matrix[i][j] << " ";
    }
    cout << endl;
  }
  cout << endl;
}

class Solution {
public:
  vector<vector<int>> merge(vector<vector<int>>& intervals) {
    vector<vector<int>> res;
    std::sort(intervals.begin(), intervals.end(), [](vector<int> interval, vector<int> interval2) {
      return interval[0] < interval2[0];
    });

    vector<int> temp = intervals[0];
    for (const auto &interval : intervals) {
      if (interval == temp)
        continue;
      if (interval[0] <= temp[1]) {
        temp[1] = interval[1];
      } else if (temp[1] < interval[0]) {
        res.push_back(temp);
        temp = interval;
      }
    }

    res.push_back(temp);
      
    return res;
  }
};

int main() {
  Solution s;
  vector<vector<int>> intervals = {{1,3},{2,6},{8,10},{5,7},{15,18}};
  
  vector<vector<int>> res = s.merge(intervals);
  printMatrix(res);
}
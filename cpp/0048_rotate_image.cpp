#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

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
  void rotate(vector<vector<int>>& matrix) {
     // std::vector<std::vector<int>> temp(matrix.size(), std::vector<int>(matrix[0].size(), 0));
    int m = matrix.size();
    int n = matrix[0].size();
    
     for (int i = 0; i < m; ++i) {
       for (int j = 0; j < i; ++j) {
         const int temp  = matrix[j][i];
         matrix[j][i] = matrix[i][j];
         matrix[i][j] = temp;
       }
     }

    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n/2; ++j) {
        int temp  = matrix[i][j];
        matrix[i][j] = matrix[i][n-j-1];
        matrix[i][n-j-1] = temp;
      }
    }
  }
};

int main() {
  Solution s;
  // vector<vector<int>> matrix = {{5,1,9,11},{2,4,8,10},{13,3,6,7},{15,14,12,16}};
  vector<vector<int>> matrix = {{1,2,3},{4,5,6}, {7,8,9}};
  printMatrix(matrix);
  s.rotate(matrix);
  printMatrix(matrix);
}

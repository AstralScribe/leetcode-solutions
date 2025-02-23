#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>

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
  void setZeroes(vector<vector<int>> &matrix) {
    int m = matrix.size();
    int n = matrix[0].size();

    unordered_set<int> idx;

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (matrix[i][j] == 0) {
          idx.insert(n * i + j);
        }
      }
    }

    for (auto it = idx.begin(); it != idx.end(); it++) {
      for (int i = 0; i < m; i++) {
        matrix[i][(*it) % n] = 0;
      }
      for (int j = 0; j < n; j++) {
        matrix[(*it) / n][j] = 0;
      }
    }
  }

  void setZeroes2(vector<vector<int>> &matrix) {
    int m = matrix.size();
    int n = matrix[0].size();

    bool row_check = false, col_check = false;
    
    for (int i = 0; i < m; i++) {
      if (matrix[i][0] == 0) {
        row_check = true;
      }
    }
      
    for (int j = 0; j < n; j++) {
      if (matrix[0][j] == 0)
        col_check = true;
    }

    for (int i = 1; i < m; i++) {
      for (int j = 1; j < n; j++) {
        if (matrix[i][j] == 0) {
          matrix[i][0] = 0;
          matrix[0][j] = 0;
        }
      }
    }

    for (int i = 1; i < m; i++) {
      if (matrix[i][0] == 0) {
        for (int j = 1; j < n; j++) {
          matrix[i][j] = 0;
        }
      }
    }

    for (int j = 1; j < n; j++) {
      if (matrix[0][j] == 0) {
        for (int i = 1; i < m; i++) {
          matrix[i][j] = 0;
        }
      }
    }
    
    if (col_check) {
      for (int j = 0; j < n; j++) {
        matrix[0][j] = 0;
      }
    }
    
    if (row_check) {
      for (int i = 0; i < m; i++) {
        matrix[i][0] = 0;
      }
    }

  }
};

int main() {
  Solution s;
  vector<vector<int>> matrix = {{1,1,1},{1,0,1},{1,1,1}};
  // vector<vector<int>> matrix = {
      // {1, 0, 2, 0}, {3, 4, 5, 2}, {1, 3, 1, 5}, {1, 2, 3, 5}};
  printMatrix(matrix);
  s.setZeroes2(matrix);

  printMatrix(matrix);
}
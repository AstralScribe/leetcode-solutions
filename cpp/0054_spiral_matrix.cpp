#include <iostream>
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

void printOutput(const vector<int> &matrix) {
  for (int i = 0; i < matrix.size(); ++i) {
    cout << matrix[i] << " ";
  }
  cout << endl;
}

class Solution {
public:
  vector<int> spiralOrder(vector<vector<int>> &matrix) {
    vector<int> output;
    int m = matrix.size();
    int n = matrix[0].size();

    int row_left = 0, row_right = n - 1;
    int col_up = 0, col_down = m - 1;

    while (row_left <= row_right && col_up <= col_down) {
      for (int i = row_left; i <= row_right; ++i) {
        output.push_back(matrix[col_up][i]);
      }
      col_up++;
      for (int i = col_up; i <= col_down; ++i) {
        output.push_back(matrix[i][row_right]);
      }
      row_right--;
      if (col_up <= col_down) {
        for (int i = row_right; i >= row_left; --i) {
          output.push_back(matrix[col_down][i]);
        }
        col_down--;
      }
      if (row_left <= row_right) {
        for (int i = col_down; i >= col_up; --i) {
          output.push_back(matrix[i][row_left]);
        }
        row_left++;
      }
    }
    return output;
  }
};

int main() {
  Solution s;
  vector<vector<int>> matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
  printMatrix(matrix);
  auto out = s.spiralOrder(matrix);
  printOutput(out);
}
#include <iostream>
#include <vector>

using namespace std;

void printMatrix(const vector<vector<int>> &matrix) {
  for (int i = 0; i < matrix.size(); ++i) {
    for (int j = 0; j < matrix[i].size(); ++j) {
      cout << matrix[i][j] << " ";
    }
    cout << endl;
  }
  cout << endl;
}

class Solution {
public:
  vector<vector<int>> generate(int numRows) {
    vector<vector<int>> matrix;

    if (numRows >= 1) {
      vector<int> temp(1);
      temp[0] = 1;
      matrix.push_back(temp);
    }

    if (numRows >= 2) {
      vector<int> temp(2);
      temp[0] = 1;
      temp[1] = 1;
      matrix.push_back(temp);
    }

    if (numRows >= 3) {
      for (int i = 3; i < numRows + 1; ++i) {
        vector<int> row(i);
        row[0] = 1;
        row[i - 1] = 1;
        for (int j = 1; j < i - 1; ++j) {
          row[j] = matrix[i - 2][j - 1] + matrix[i - 2][j];
        }
        matrix.push_back(row);
      }
    }
    return matrix;
  }

  vector<vector<int>> generate2(int numRows) {
    vector<vector<int>> matrix;

    for (int i = 1; i <= numRows; ++i) {
      int coeff = 1;
      vector<int> row(i);
      row[0] = 1;
      
      for (int j = 1; j <= i; ++j) {
        coeff = coeff * (i-j);
        coeff = coeff / j;
        row[j] = coeff;
      }
      matrix.push_back(row);
    }
    return matrix;
  }
};

int main() {
  Solution s;
  vector<vector<int>> result = s.generate2(5);
  printMatrix(result);
}
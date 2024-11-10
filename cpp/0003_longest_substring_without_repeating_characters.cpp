#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
 public:
  int lengthOfLongestSubstring(string s) {
    int len_substring = 0, counter = 0;
    int length_string = s.length();
    vector<char> seen;

    for (char c : s) {
      bool present = false;
      for (auto i : seen) {
        if (i == c) present = true;
        counter++;
      }
      if (present) {
        auto X = seen.size() - counter + 1;
        vector<int> result(X);

      } else {
        counter += 1;
        seen[c] = 1;
      }
    }

    return len_substring;
  }
};

int main() {
  Solution s;
  int length = s.lengthOfLongestSubstring("hello");
  cout << length << endl;
}

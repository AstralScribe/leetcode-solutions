#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
  vector<string> generateParenthesis(int n) {
    std::vector<string> result;
    std::string current_string{};
    recursive_track (n, current_string, 0, result);
    return result;
  }

  void recursive_track(int current_num, std::string& current_string, int count, std::vector<string>& result){
    if (current_num == 0 && count != 0){
      current_string.append(count, ')');
      result.push_back(current_string);
      return;
    } else if (current_num != 0 && count == 0) {
      current_string = current_string+'(';
      count++;
      current_num--;
      recursive_track(current_num, current_string, count, result);
    } else if (current_num != 0 && count != 0){
      auto new_string_open = current_string+'(';      
      auto new_string_closed = current_string+')';      
      recursive_track(current_num - 1, new_string_open, count + 1, result);
      recursive_track(current_num, new_string_closed, count - 1, result);
    }
  }
};
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        def recursive_track(current_num, current_string_list, count, stack):
            if current_num == 0 and count == 0:
                return
            elif current_num == 0 and count != 0:
                current_string_list += [")"] * count
                stack.append("".join(current_string_list))
                return
            elif current_num != 0 and count == 0:
                current_string_list.append("(")
                count += 1
                current_num -= 1
                recursive_track(current_num, current_string_list, count, stack)
            elif current_num != 0 and count != 0:
                recursive_track(current_num-1, current_string_list+["("], count + 1, stack)
                recursive_track(current_num, current_string_list+[")"], count - 1, stack)

        recursive_track(n, [], 0, stack)

        return stack


s = Solution()
n = 3
output = ["((()))", "(()())", "(())()", "()(())", "()()()"]

print(s.generateParenthesis(n))


def test_solution1():
    s = Solution()
    n = 1
    output = ["()"]

    assert s.generateParenthesis(n) == output


def test_solution2():
    s = Solution()
    n = 3
    output = ["((()))", "(()())", "(())()", "()(())", "()()()"]

    assert s.generateParenthesis(n) == output

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        output = []
        string = ""

        while True:
            if n != 0 and len(stack) == 0:
                stack.append(")")
                string += "("
                n -= 1

            if n != 0 and len(stack) != 0:







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

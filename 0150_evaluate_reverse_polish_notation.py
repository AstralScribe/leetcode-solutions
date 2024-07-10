from typing import List 

# Pythonic Solution:
# Security vulnerablity due to use of eval on input value.
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        answer_stack =  []
        for token in tokens:
            if token in ["+","-","*","/"]:
                rhs = answer_stack.pop()
                lhs = answer_stack.pop()
                eval_string = lhs+token+rhs
                answer_stack.append(str(int(eval(eval_string))))
            else:
                answer_stack.append(token)
            print(answer_stack)
        return int(answer_stack.pop())


# Non Pythonic Solution
class Solution2:
    def evalRPN(self, tokens: List[str]) -> int:
        answer_stack =  []
        for token in tokens:
            if token in ["+","-","*","/"]:
                rhs = answer_stack.pop()
                lhs = answer_stack.pop()
                if token == "+":
                    answer_stack.append(lhs+rhs)
                elif token == "-":
                    answer_stack.append(lhs-rhs)
                elif token == "*":
                    answer_stack.append(lhs*rhs)
                elif token == "/":
                    answer_stack.append(int(lhs/rhs))
            else:
                answer_stack.append(int(token))
            print(answer_stack)
        return answer_stack.pop()


def test_solution():
    s = Solution()
    s2 = Solution2()
    tokens = ["2","1","+","3","*"]
    assert s.evalRPN(tokens) == 9
    assert s2.evalRPN(tokens) == 9

def test_solution2():
    s = Solution()
    s2 = Solution2()
    tokens = ["4","13","5","/","+"]
    assert s.evalRPN(tokens) == 6
    assert s2.evalRPN(tokens) == 6

def test_solution3():
    s = Solution()
    s2 = Solution2()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    assert s.evalRPN(tokens) == 22
    assert s2.evalRPN(tokens) == 22


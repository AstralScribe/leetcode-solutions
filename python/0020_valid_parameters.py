class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] not in ["(", "{", "["]:
            return False

        mapper_stack = {"(":")", "[":"]", "{":"}"}
        bracket_stack = [] 
        valid_stack = True
        for chr in s:
            if chr in [")", "}", "]"]:
                valid_stack = False

            if chr in mapper_stack:
                bracket_stack.append(mapper_stack[chr])
                continue

            if len(bracket_stack) and bracket_stack[-1] == chr:
                bracket_stack.pop()
                valid_stack = True

            if not valid_stack:
                return False

        return not bool(len(bracket_stack))


def run_test(string: str):
    s = Solution()
    val = s.isValid(string)
    return val

if __name__ == "__main__":
    nums =  "({[]})"
    val = run_test(nums)
    print(val)

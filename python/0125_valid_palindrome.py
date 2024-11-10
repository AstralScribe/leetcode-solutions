class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        count_range = len(s)
        l = 0
        r = count_range-1

        while l < r:
            if s[l] == " " or not s[l].isalnum():
                l = l+1
                continue
            if s[r] == " " or not s[r].isalnum():
                r = r-1
                continue
            if s[l] != s[r]:
                return False
            l = l+1
            r = r-1
        return True


s = Solution()

def test_solution1():
    input_string =  "A man, a plan, a canal: Panama"
    assert s.isPalindrome(input_string) is True

def test_solution2():
    input_string =  "race a car"    
    assert s.isPalindrome(input_string) is False

def test_solution3():
    input_string =  " "    
    assert s.isPalindrome(input_string) is True

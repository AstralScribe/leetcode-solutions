from typing import List

# Double for loop solution 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        num_vars = len(temperatures)
        output = []
        for i in range(num_vars):
            for j in range(i, num_vars):
                if temperatures[j]>temperatures[i]:
                    output.append(j-i)
                    break
                if j == num_vars-1:
                    output.append(0)


        return output



# Stack?
class Solution2:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ...



def test_solution():
    s = Solution()
    assert s.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
    s2 = Solution2()
    assert s2.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]

def test_solution2():
    s = Solution()
    assert s.dailyTemperatures([30,40,50,60]) == [1,1,1,0]
    s2 = Solution2()
    assert s2.dailyTemperatures([30,40,50,60]) == [1,1,1,0]


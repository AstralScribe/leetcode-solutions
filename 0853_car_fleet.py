from typing import List

# Python: Recursion?
class Solution:
    def recursive_fleet(fleet):
        fleet1 = []
        j=0
        for i in range(len(fleet)):
            if i == 0:
                fleet1.append([fleet[i][0]+fleet[i][1], fleet[i][1]])
                j+=1
            else:
                if fleet[i][0]+fleet[i][1]>=fleet[i-1][0]+fleet[i-1][1]:
                    fleet1[j-1][1] = min(fleet[i][1], fleet1[j-1][1])
                else:
                    fleet1.append([fleet[i][0]+fleet[i][1], fleet[i][1]])
                    j+=1
        return fleet1

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet0 = [[p,s] for p, s in zip(position, speed)]
        fleet0.sort(reverse=True)
        print(fleet0)
        

# Pyhton: Other method?
class Solution2:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ...
        



target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

s = Solution()
s.carFleet(target=target, position=position, speed=speed)


def test_solution():
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]

    s = Solution()
    assert s.carFleet(target=target, position=position, speed=speed) == 3
    
def test_solution2():
    target = 100
    position = [0,2,4]
    speed = [4,2,1]

    s = Solution()
    assert s.carFleet(target=target, position=position, speed=speed) == 1
    

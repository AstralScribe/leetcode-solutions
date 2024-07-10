from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet0 = [[p,s] for p, s in zip(position, speed)]
        fleet1 = []
        j=0
        for i in range(len(fleet0)):
            if i == 0:
                fleet1.append([fleet0[i][0]+fleet0[i][1], fleet0[i][1]])
                j+=1
            else:
                if fleet0[i][0]+fleet0[i][1]>=fleet0[i-1][0]+fleet0[i-1][1]:
                    fleet1[j-1][1] = min(fleet0[i][1], fleet1[j-1][1])
                else:
                    fleet1.append([fleet0[i][0]+fleet0[i][1], fleet0[i][1]])
                    j+=1




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
    

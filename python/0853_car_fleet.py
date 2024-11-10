from typing import List

# Python: Recursion?
class Solution:
    def recursive_fleet(self, fleet, target, count):
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

        if fleet[0][0] >= target:
            count+=1

        count =self.recursive_fleet(fleet, target, count)

        

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet0 = [[p,s] for p, s in zip(position, speed)]
        fleet0.sort(reverse=True)
        print(fleet0)
        print(self.recursive_fleet(fleet0, target, 0))
        

# Pyhton: Other method? Pushing slower times into a stack and calculating len.
class Solution2:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet0 = [(p,s) for p, s in zip(position, speed)]
        fleet0.sort(reverse=True)
        all_times = [(target-fleet0[0][0])/fleet0[0][1]]
        fleet0.pop(0)
        for fleet in fleet0:
            time_taken = (target-fleet[0]) / fleet[1]
            if time_taken > all_times[-1]:
                all_times.append(time_taken)
        
        return len(all_times)


target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

s = Solution2()
s.carFleet(target=target, position=position, speed=speed)


def test_solution():
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]

    s = Solution2()
    assert s.carFleet(target=target, position=position, speed=speed) == 3
    
def test_solution2():
    target = 100
    position = [0,2,4]
    speed = [4,2,1]

    s = Solution2()
    assert s.carFleet(target=target, position=position, speed=speed) == 1
    

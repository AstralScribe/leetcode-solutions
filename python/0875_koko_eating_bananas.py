from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            pivot = (left + right) // 2
            time_taken = sum((pile + pivot - 1) // pivot for pile in piles)

            if time_taken > h:
                left = pivot + 1
            else:
                right = pivot

        return left


# Fastest solution on leetcode. Study to understand
class Solution2:
    def minEatingSpeed(self, piles: List[int], max_hours: int) -> int:
        # Number of piles of bananas
        num_piles = len(piles)

        # Maximum number of bananas in a single pile
        max_pile = max(piles)

        # Total number of bananas
        total_bananas = sum(piles)

        # Helper function to calculate the total time (hours) taken
        # to eat all bananas at a given eating speed
        def hours_needed(speed):
            # Calculate time to finish each pile with the given speed, then sum up
            return sum(math.ceil(pile / speed) for pile in piles)

        # Define the range for binary search:
        # Start of range: Minimum possible speed, which is total bananas divided by max_hours
        left = math.ceil(total_bananas / max_hours)

        # End of range: If each hour is dedicated to only one pile, the max speed needed is the largest pile size
        right = (
            max_pile
            if max_hours == num_piles
            else math.ceil(total_bananas / (max_hours - num_piles))
        )

        # Binary search to find the minimum eating speed that completes within max_hours
        while left < right:
            # Calculate the middle speed
            mid_speed = (left + right) // 2

            # Check if this speed allows finishing all piles within max_hours
            if hours_needed(mid_speed) <= max_hours:
                # If so, it may be possible to go slower, so reduce the right bound
                right = mid_speed
            else:
                # Otherwise, increase the left bound to search faster speeds
                left = mid_speed + 1

        # Return the minimum speed found that allows completion within max_hours
        return left


s = Solution()
piles = [1, 4, 3, 2]
h = 9

assert s.minEatingSpeed(piles, h) == 2


def test_solution():
    s = Solution()
    piles = [3, 6, 7, 11]
    h = 8

    assert s.minEatingSpeed(piles, h) == 4


def test_solution2():
    s = Solution()
    piles = [30, 11, 23, 4, 20]
    h = 5

    assert s.minEatingSpeed(piles, h) == 30


def test_solution3():
    s = Solution()
    piles = [1, 4, 3, 2]
    h = 9

    assert s.minEatingSpeed(piles, h) == 2

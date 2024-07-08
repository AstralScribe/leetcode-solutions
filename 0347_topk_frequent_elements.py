from collections import Counter
from typing import List

# Pythonic (Using python methods)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = Counter(nums)
        out = dict(temp.most_common()[:k])
        return list(out.keys())


# Non-Pythonic (Generic, can be duplicated in other langs)
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ...

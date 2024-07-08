from typing import List
from collections import defaultdict

# Pythonic (Using python methods)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = defaultdict(list)
        for word in strs:
            temp = "".join(sorted(word))
            out[temp].append(word)

        return list(out.values())

# Non-Pythonic (Generic, can be duplicated in other langs)
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ...

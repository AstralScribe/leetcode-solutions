from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = defaultdict(list)
        for word in strs:
            temp = "".join(sorted(word))
            out[temp].append(word)

        return list(out.values())

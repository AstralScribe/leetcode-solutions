class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cs, ct = {}, {}

        for i, j in zip(s, t):
            cs[i] = 1 + cs.get(i, 0)
            ct[j] = 1 + ct.get(j, 0)

        return cs == ct

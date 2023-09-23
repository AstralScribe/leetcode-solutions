from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = Counter(nums)
        out = dict(temp.most_common()[:k])
        return list(out.keys())

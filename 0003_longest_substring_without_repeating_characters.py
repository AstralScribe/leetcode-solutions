class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = list(s)
        hashmap = []
        length = 0
        
        for i in string:
            if i not in hashmap:
                hashmap.append(i)
                temp = len(hashmap)
                if temp > length:
                    length = temp
            else:
                idx = hashmap.index(i)
                hashmap = hashmap[idx+1:]
                hashmap.append(i)
                
        return length

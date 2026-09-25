class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # map_s = dict()
        # map_t = dict()
        # for c in s:
        #     map_s.update
        # for c in t:
        # return map_s == map_t
        return sorted(s) == sorted(t)
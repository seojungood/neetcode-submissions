class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # map_s = dict()
        # map_t = dict()
        # for c in s:
        #     map_s.update()
        # for c in t:
        # return map_s == map_t
        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True
        # return sorted(s) == sorted(t)
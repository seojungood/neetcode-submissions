class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # countS, countT = {}, {}

        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i],0)
        #     countT[t[i]] = 1 + countT.get(t[i],0)
        # for c in countS:
        #     if countS[c] != countT.get(c,0):
        #         return False
        # return True

        # return Counter(s) == Counter(t)
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())
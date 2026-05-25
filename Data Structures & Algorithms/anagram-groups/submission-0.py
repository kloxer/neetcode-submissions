class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            sort = sorted(s)
            joined = "".join(sort)
            if joined not in seen:
                seen[joined] = [s]
            else:
                seen[joined].append(s)

        ret = []
        for k,v in seen.items():
            print(v)
            ret.append(v)
        return ret
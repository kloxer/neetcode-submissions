class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #bruteforce below, sort the strings first then check if in dictionary
        # O (m x nlogn) time complexity
        # seen = {}
        # for s in strs:
        #     sort = sorted(s)
        #     joined = "".join(sort)
        #     if joined not in seen:
        #         seen[joined] = [s]
        #     else:
        #         seen[joined].append(s)

        # ret = []
        # for k,v in seen.items():
        #     ret.append(v)
        # return ret
        
        #what about a more efficient solution?
        chars = {}
        for s in strs:
            count = [0] * 26 #going to be our a ... z
            for c in s:
               count[ord(c) - ord("a")] += 1
    
            count = tuple(count)
            if count not in chars:
                chars[count] = [s]
            else:
                chars[count].append(s)

        return list(chars.values())

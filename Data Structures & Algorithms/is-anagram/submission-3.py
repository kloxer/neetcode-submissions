class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        seenT = {}
        for c in s:
            if c not in seen:
                seen[c] = 1
            else:
                seen[c] += 1
        
        for c in t:
            if c not in seenT:
                seenT[c] = 1
            else:
                seenT[c] += 1
        
        for k,v in seen.items():
            if k not in seenT:
                return False
            if seenT[k] != v:
                return False
        print(seenT)
        return True
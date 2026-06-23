class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen =  {}

        for x in nums:
            if x not in seen:
                seen[x] = 1
            else:
                seen[x] +=1

        freq = [[] for i in range(len(nums) + 1)]
        print(freq)
        for c,v in seen.items():
            freq[v].append(c)

        print(freq)
        ret = []
        for c in range(len(freq)-1, -1, -1):
            if freq[c]:
                for n in freq[c]:
                    if len(ret) < k:
                        ret.append(n)
            
        return ret



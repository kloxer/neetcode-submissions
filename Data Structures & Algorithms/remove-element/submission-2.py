class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #thinking about using 2 passes
        #one time just rearrange it
        #next time replace 2 with random stuff
        tmp = []
        for x in nums:
            if x != val:
                tmp.append(x)
        for i in range(len(tmp)):
            nums[i] = tmp[i]
        return len(tmp)
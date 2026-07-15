class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #thinking about using 2 passes
        #one time just rearrange it
        #next time replace 2 with random stuff

        for i in range(len(nums)):
            if nums[i] == val:
                for j in range(i+1,len(nums)):
                    print(i,j)
                    if nums[j] != val:
                        tmp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = tmp
                        break
        cnt = 0
        for i in range(len(nums)):
            if nums[i] != val:
                cnt += 1

        return cnt
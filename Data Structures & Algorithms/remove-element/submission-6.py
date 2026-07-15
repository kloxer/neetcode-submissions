class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #brute force below
        # tmp = []
        # for x in nums:
        #     if x != val:
        #         tmp.append(x)
        # print(tmp)
        # for i in range(len(tmp)):
        #     nums[i] = tmp[i]
        #     print(nums)

        # return len(tmp)
        
        #what about 2 pointers
        i=0
        j=len(nums) - 1
        if i == j:
            return 0
        while i <= j:
            while nums[j] == val and i<j:
                j -= 1
            print(nums[j])
            if nums[i] == val:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
            print(nums)
            i += 1
        print(nums)
        cnt = 0
        for x in nums:
            if x != val:
                cnt += 1

        return cnt
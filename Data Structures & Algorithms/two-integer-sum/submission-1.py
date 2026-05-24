class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return []
        seen = {}
        for i in range(len(nums)):
            res = target - nums[i]
            if res not in seen:
                seen[nums[i]] = i
                # 3 : 0
            else:
                if i < seen[res]:
                    return [i,res]
                return [seen[res],i]
        return []





                
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        tempSum = 0
        consecutiveOnes = 0

        for x in range(0, len(nums)):
            if nums[x] == 1: 
                tempSum += 1
                consecutiveOnes = max(consecutiveOnes, tempSum)
            else:
                tempSum = 0

        return consecutiveOnes 
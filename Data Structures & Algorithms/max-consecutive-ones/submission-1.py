class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        tempSum = 0
        consecutiveOnes = 0

        for x in range(0, len(nums)):
            consecutiveOnes = max(consecutiveOnes, tempSum)
            if nums[x] == 1: 
                print(x, nums[x] )
                tempSum += 1
            else:
                print(tempSum)
                tempSum = 0
        
        return max(consecutiveOnes, tempSum) 
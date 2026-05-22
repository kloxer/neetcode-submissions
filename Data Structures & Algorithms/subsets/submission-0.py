class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        allLists = []
        buildList = []

        def dfs(i):
            if i >= len(nums):
                allLists.append(buildList.copy())
                print(allLists)
                return
            buildList.append(nums[i])
            dfs(i = i + 1)
            buildList.pop()
            dfs(i = i + 1)
        dfs(0)

        return allLists

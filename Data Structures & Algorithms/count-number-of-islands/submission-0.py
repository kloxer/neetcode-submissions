class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        seen = set()

        def dfs(i,j):
            if (i < 0 or j < 0 or i >= rows or j >= cols or (i,j) in seen):
                return
            print(i,j)
            if (grid[i][j] == '0'):
                return
            seen.add((i,j)) #add the path
            #visit all around 
            dfs(i, j+1)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i-1, j)


        total = 0
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in seen and grid[i][j] == '1':
                    total +=1
                    dfs(i,j)
        return total


        
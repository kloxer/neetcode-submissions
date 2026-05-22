class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        q = deque()
        fresh  = 0
        def isFresh(r,c):
            nonlocal fresh
            if r < 0 or c <0 or r >= rows or c>= cols or grid[r][c] != 1:
                return 
            print(r,c)
            grid[r][c] = 2
            q.append([r,c])
            fresh = fresh - 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])

        timeElapsed = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                isFresh(r+1,c)
                isFresh(r-1,c)
                isFresh(r,c+1)
                isFresh(r,c-1)

            timeElapsed+=1


        if fresh > 0:
            return -1

        return timeElapsed 
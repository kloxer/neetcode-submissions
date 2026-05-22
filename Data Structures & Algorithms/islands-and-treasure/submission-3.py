class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols = len(grid), len(grid[0])
        queue  = deque()
        seen = set()

        def addRoom(r,c, steps):
            if r < 0 or c < 0 or r>= rows or c>= cols or grid[r][c] == -1 or (r,c) in seen:
                return

            seen.add((r,c))
            queue.append([r,c])



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append([r,c])
                    seen.add((r,c))
        
        dist = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                grid[r][c] = dist

                addRoom(r+1,c,dist)
                addRoom(r-1,c,dist)
                addRoom(r,c+1,dist)
                addRoom(r,c-1,dist)
            dist += 1


            
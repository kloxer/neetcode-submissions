class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        pacific = False
        atlantic = False

        seen = set()
        def dfs(r,c, prev):
            nonlocal pacific
            nonlocal atlantic

            if r < 0 or c < 0:
                #reached pacific
                pacific = True
                return

            if r >= rows or c >= cols:
                #reached atlantic
                atlantic = True
                return

            if heights[r][c] > prev or (r,c) in seen:
                #means its bigger then the previous
                #water cant lfow this way
                #return
                return
            
            seen.add((r,c))
            dfs(r-1,c,heights[r][c])
            dfs(r+1,c, heights[r][c])
            dfs(r,c+1,heights[r][c])
            dfs(r,c-1,heights[r][c])

        answers = []
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,123123213123)
                if pacific and atlantic:
                    print("reached")
                    print(r,c)
                    answers.append([r,c])
                pacific = False
                atlantic = False
                seen  = set()
        return answers
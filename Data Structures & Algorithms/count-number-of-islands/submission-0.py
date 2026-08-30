class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        def dfs(x,y):

            if x<0 or x>=rows or y<0 or y>=cols:
                return
            if grid[x][y] == "0":
                return
            if (x,y) in visited:
                return 
            
            visited.add((x,y))

            dfs(x+1,y)
            dfs(x,y+1)
            dfs(x-1,y)
            dfs(x,y-1)

        islands = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i,j) not in visited:
                    dfs(i,j)
                    islands +=1
        return islands
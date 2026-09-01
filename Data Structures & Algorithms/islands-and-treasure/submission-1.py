class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        q = deque()

        def bfs(x,y):
            if x<0 or x>= rows or y<0 or y>=cols or (x,y) in visited or grid[x][y] == -1:
                return 
            visited.add((x,y))
            q.append([x,y])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))

        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                bfs(r+1,c)
                bfs(r,c+1)
                bfs(r-1,c)
                bfs(r,c-1)
            dist +=1
        


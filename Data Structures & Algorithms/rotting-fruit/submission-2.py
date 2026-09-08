class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        visited = set()
        
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh = 0

        def rot(r,c):
            nonlocal fresh
            if r<0 or r>rows-1 or c<0 or c>cols-1 or (r,c) in visited or grid[r][c] !=1:
                return
            fresh -= 1
            q.append([r,c])
            visited.add((r,c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visited.add((r,c))
                if grid[r][c] == 1:
                    fresh += 1

        time = -1
        print(f"fresh before traversing {fresh}")
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                rot(r+1,c)
                rot(r-1,c)
                rot(r,c+1)
                rot(r,c-1)
            time +=1
        print(f"fresh after traversing {fresh}")
        
        if fresh >0:
            return -1
        if time == -1:
            return 0
        return time

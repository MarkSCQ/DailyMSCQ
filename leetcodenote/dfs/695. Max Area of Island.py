"""
https://leetcode.com/problems/max-area-of-island/solution/




"""
# ! DFS solution


class Solution1:
    def maxAreaOfIsland(self, grid):
        height = len(grid)
        width = len(grid[0])

        score = 0

        for row in range(height):
            for col in range(width):
                if grid[row][col]:
                    score = max(score, self.helper(
                        grid, height, width, row, col))

        return score

    def helper(self, grid, height, width, row, col):

        if row < 0 or row >= height:
            return 0
        if col < 0 or col >= width:
            return 0

        if grid[row][col] == 0:
            return 0

        grid[row][col] = 0

        return 1+self.helper(grid, height, width, row+1, col) +\
            self.helper(grid, height, width, row-1, col) +\
            self.helper(grid, height, width, row, col+1) +\
            self.helper(grid, height, width, row, col-1)



class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        DIR = [0, 1, 0, -1, 0]
        
        def bfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = 0
            ans = 0
            while q:
                r, c = q.popleft()
                ans += 1
                for i in range(4):
                    nr, nc = r + DIR[i], c + DIR[i+1]
                    if nr < 0 or nr == m or nc < 0 or nc == n or grid[nr][nc] == 0: continue
                    grid[nr][nc] = 0  # Mark this square as visited
                    q.append((nr, nc))
            return ans
        
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    ans = max(ans, bfs(r, c))
        return ans


        
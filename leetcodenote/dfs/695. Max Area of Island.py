"""
https://leetcode.com/problems/max-area-of-island/solution/




"""
# ! DFS solution


from collections import deque


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


"""
! BFS

"""


class Solution2:
    def maxAreaOfIsland(self, grid):

        m, n = len(grid), len(grid[0])
        DIR = [0, 1, 0, -1, 0]


        def bfs(r, c):
            # ! initilize deque to store land and sea cell around current "1"
            q = deque([(r, c)])
            grid[r][c] = 0
            ans = 0
            while q:
                r, c = q.popleft()
                ans += 1
                # ! searching four different directions
                for i in range(4):
                    nr, nc = r + DIR[i], c + DIR[i+1]
                    # ! boundary check and if the current is sea then skip
                    if nr < 0 or nr == m or nc < 0 or nc == n or grid[nr][nc] == 0:
                        continue
                    # ! mark the current visisted 1 as 0
                    grid[nr][nc] = 0  
                    q.append((nr, nc))
            return ans

        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    # ! update the current max value
                    ans = max(ans, bfs(r, c))
        return ans

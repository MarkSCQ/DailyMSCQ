"""
DFS:

! start from four edges to find optimal cells

"""


class Solution:

    def pacificAtlantic(self, heights):
    
    # ! check validation of input
        if not heights:
            return heights

        m = len(heights)
        n = len(heights[0])

        pvisited = set()
        avisited = set()

        direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(visited, x, y):
            visited.add((x, y))
            for dx, dy in direction:
                new_x, new_y = x+dx, y+dy
                if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) not in visited and heights[new_x][new_y] >= heights[x][y]:
                    dfs(visited, new_x, new_y)

        for i in range(m):
            dfs(pvisited, i, 0)
            dfs(avisited, i, n-1)

        for j in range(m):
            dfs(pvisited, 0, j)
            dfs(avisited, m-1, j)
            
        return list(pvisited.intersection(avisited))

"""
DFS:

! start from four edges to find optimal cells

"""


class Solution:

    def pacificAtlantic(self, heights):
        if not heights:
            return heights

        height = len(heights)
        width = len(heights[0])

        pvisited = set()
        avisited = set()

        direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(visited, x, y):
            visited.add((x, y))
            for dx, dy in direction:

                new_x, new_y = x+dx, y+dy

                if new_x >= height or new_y >= width or new_x < 0 or new_y < 0:
                    continue
                if (new_x, new_y) in visited:
                    continue
                if heights[new_x][new_y] < heights[x][y]:
                    continue
                dfs(visited, new_x, new_y)

        for i in range(height):
            dfs(pvisited, i, 0)
            dfs(avisited, i, width-1)

        for j in range(width):
            dfs(pvisited, 0, j)
            dfs(avisited, height-1, j)

        return list(pvisited.intersection(avisited))


"""
BFS
"""


class Solution2:

    def pacificAtlantic(self, heights):
        height = len(heights)
        width = len(heights[0])

"""
https://leetcode.com/problems/flood-fill/

An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.


Example 1:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Example 2:
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],[2,2,2]]


"""

"""
DFS recursion
Runtime: 114 ms, faster than 18.85% of Python3 online submissions for Flood Fill.
Memory Usage: 14.4 MB, less than 52.53% of Python3 online submissions for Flood Fill.
"""


class Solution:
    def floodFill(self, image, sr, sc, newColor):

        color = image[sr][sc]
        height = len(image)
        width = len(image[0])

        def dfsChanging(oc, row, col, image, nc):
            if image[row][col] == oc:
                image[row][col] = nc
                if row >= 1:
                    dfsChanging(oc, row-1, col, image, nc)
                if col >= 1:
                    dfsChanging(oc, row, col-1, image, nc)
                if row+1 < height:
                    dfsChanging(oc, row+1, col, image, nc)
                if col+1 < width:
                    dfsChanging(oc, row, col+1, image, nc)

        if color != newColor:
            # perform color dfs changing

            dfsChanging(color, sr, sc, image, newColor)

        # return the modified image
        return image


"""
DFS Iteration
"""


class Solution:
    def floodFill(self, image, sr, sc, newColor):

        color = image[sr][sc]
        height = len(image)
        width = len(image[0])

        dire = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        stack = [(sr, sc)]

        while stack:

            row, col = stack.pop()
            if row < 0 or row >= height or col < 0 or col >= width:
                continue
            if image[row][col] != color:
                continue

            image[row][col] = newColor

            for i in range(len(dire)):
                nrow = row+dire[i][0]
                ncol = col+dire[i][1]

                stack.append((nrow, ncol))
        return image


"""
BFS

"""


class Solution:
    def floodFill(self, image, sr, sc, newColor):
        from collections import deque
        old, m, n = image[sr][sc], len(image), len(image[0])
        if old != newColor:
            q = deque([(sr, sc)])
            while q:
                i, j = q.popleft()
                image[i][j] = newColor
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n and image[x][y] == old:
                        q.append((x, y))
        return image

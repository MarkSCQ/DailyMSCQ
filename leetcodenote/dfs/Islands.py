def solve(grid):
    # write code here
    def dfshelper(grid, row, col, height, width):
        if row < 0 or row >= height or col < 0 or col >= width or grid[row][col]==0:
            return 0

        if grid[row][col] == 1:
            grid[row][col] = 0
        dfshelper(grid, row+1, col, height, width)
        dfshelper(grid, row-1, col, height, width)
        dfshelper(grid, row, col+1, height, width)
        dfshelper(grid, row, col-1, height, width)

    count = 0

    height = len(grid)
    width = len(grid[0])

    for row in range(height):
        for col in range(width):
            if grid[row][col] == 1:
                dfshelper(grid, row, col, height, width)
                count += 1
    return count


grid = [[1, 1, 0, 0, 0],
        [0, 1, 0, 1, 1],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1]]


print(solve(grid))

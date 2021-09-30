// Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

// An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

// Example 1:

// Input: grid = [
//  ["1","1","1","1","0"],
//  ["1","1","0","1","0"],
//  ["1","1","0","0","0"],
//  ["0","0","0","0","0"]
// ]
// Output: 1

// Example 2:
// Input: grid = [
//  ["1","1","0","0","0"],
//  ["1","1","0","0","0"],
//  ["0","0","1","0","0"],
//  ["0","0","0","1","1"]
// ]
// Output: 3


class Solution {
public:
    void dfs(std::vector<std::vector<char>> &grid, int x, int y)
    {
        if (x < 0 || y < 0 || x >= grid.size() || y >= grid[0].size() || grid[x][y] == '0')
            return;
        grid[x][y] = '0';
        dfs(grid, x - 1, y);
        dfs(grid, x + 1, y);
        dfs(grid, x, y - 1);
        dfs(grid, x, y + 1);
    }

    int numIslands(std::vector<std::vector<char>> &grid)
    {
        int island = 0;
        for (int x = 0; x < grid.size(); x++)
        {
            for (int  y= 0; y < grid[0].size(); y++)
            {
                if (grid[x][y] == '1')
                {
                    island++;
                    dfs(grid, x, y);
                }
            }
        }
        return island;
    }
};

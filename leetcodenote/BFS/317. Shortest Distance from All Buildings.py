"""
You are given an m x n grid grid of values 0, 1, or 2, where:

each 0 marks an empty land that you can pass by freely,
each 1 marks a building that you cannot pass through, and
each 2 marks an obstacle that you cannot pass through.
You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.


Example 1:
Input: grid = [
                [1,0,2,0,1],
                [0,0,0,0,0],
                [0,0,1,0,0]
            ]
Output: 7
Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
So return 7.

Example 2:
Input: grid = [[1,0]]
Output: 1

Example 3:
Input: grid = [[1]]
Output: -1

"""

"""
BFS, Search: Starting from buildings to empty lands

Performance:
Runtime: 9212 ms, faster than 6.59% of Python3 online submissions for Shortest Distance from All Buildings.
Memory Usage: 15 MB, less than 19.24% of Python3 online submissions for Shortest Distance from All Buildings.

"""


class Solution:
    """
    Intuition:


    """

    def shortestDistance(self, grid):
        # ! grid matrix

        totalhouse = 0
        mindis = float('inf')
        height = len(grid)
        width = len(grid[0])
        # ! distance matrix record the distance between target
        # ! distance matrix is 3 dimensional, row, width, [distance, current target building]
        distance = [[[0 for i in range(2)]for j in range(width)]
                    for i in range(height)]
        from collections import deque

        # ! applying bfs on each building
        def bfs(grid, distance, row, col):
            dires = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            queue = deque()
            queue.append((row, col))

            # ! matrix to track the visited cell
            visited = [[False for i in range(width)]for j in range(height)]
            visited[row][col] = True
            # ! count the step of walking to one building
            step = 0
            # ! caluculate the distance matrix
            while queue:
                size = len(queue)

                for i in range(size):
                    row, col = queue.popleft()
                    if grid[i][j] == 0:
                        # ! if current land is empty, then calcualte its steps and mark its building
                        distance[row][col][0] += step
                        distance[row][col][1] += 1
                    # ! trial for the next step
                    for i in range(len(dires)):
                        nrow = row + dires[i][0]
                        ncol = col + dires[i][1]
                        # ! boundary check
                        if 0 <= nrow < height and 0 <= ncol < width:
                            # ! if not visited and the cell happens to be empty, add to the queue
                            if visited[nrow][ncol] == False and grid[nrow][ncol] == 0:
                                visited[nrow][ncol] = True
                                queue.append((nrow, ncol))
                # ! after finishing the current round, step+1
                # ! (the for loop functions as moving one step to the next cell.)
                step += 1
        # ! apply bfs on each building cell
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    totalhouse += 1
                    bfs(grid, distance, i, j)
        # ! searching for the min distance
        for i in range(height):
            for j in range(width):
                if distance[i][j][1] == totalhouse:
                    mindis = min(mindis, distance[i][j][0])
        # ! if we cannot find the min distance
        if mindis == float('inf'):
            return -1

        return mindis


"""

Runtime: 4372 ms, faster than 48.37% of Python3 online submissions for Shortest Distance from All Buildings.
Memory Usage: 14.6 MB, less than 66.71% of Python3 online submissions for Shortest Distance from All Buildings.

"""


class Solution:
    def shortestDistance(self, grid):
        mindis = float('inf')
        dires = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # ! emptyLandVal, similar as the second value of distance matrix's thrid dimension.
        # ! Mark current processed building.
        # ! Since distance is positive value, it would be better to use negative value to mark it
        emptyLandVal = 0
        height = len(grid)
        width = len(grid[0])
        # ! distance counter
        total = [[0 for j in range(width)] for i in range(height)]

        from collections import deque
        for row in range(height):
            for col in range(width):
                # ! starting from one building cell
                if grid[row][col] == 1:

                    mindis = float('inf')
                    queue = deque()
                    queue.append((row, col))
                    # ! steps counter
                    steps = 0

                    while queue:
                        # ! steps + 1,
                        steps += 1
                        size = len(queue)
                        # ! process the current cells waiting in the queue
                        for _ in range(size):
                            r, c = queue.popleft()

                            for i in range(len(dires)):
                                nrow = r+dires[i][0]
                                ncol = c+dires[i][1]
                                if 0 <= nrow < height and 0 <= ncol < width and grid[nrow][ncol] == emptyLandVal:
                                    grid[nrow][ncol] -= 1
                                    total[nrow][ncol] += steps

                                    queue.append((nrow, ncol))
                                    # ! update min distance
                                    mindis = min(mindis, total[nrow][ncol])
                    # ! update mark
                    emptyLandVal -= 1
        if mindis == float('inf'):
            return -1
        return mindis


"""
class Solution {
    public int shortestDistance(int[][] grid) {
        ! // Next four directions.
        int dirs[][] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        
        int rows = grid.length;
        int cols = grid[0].length;
        
        ! // Total Matrix to store total distance sum for each empty cell.
        int[][] total = new int[rows][cols];

        int emptyLandValue = 0;
        int minDist = Integer.MAX_VALUE;

        for (int row = 0; row < rows; ++row) {
            for (int col = 0; col < cols; ++col) {
                ! // Start a BFS from each house. 
                if (grid[row][col] == 1) {
                    minDist = Integer.MAX_VALUE;
                    ! // Use a queue to perform a BFS, starting from the cell at (r, c).
                    Queue<int[]> q = new LinkedList<>();
                    q.offer(new int[]{ row, col });
                    int steps = 0;
                    while (!q.isEmpty()) {
                        steps++;
                        for (int level = q.size(); level > 0; --level) {
                            int[] curr = q.poll();

                            for (int[] dir : dirs) {
                                int nextRow = curr[0] + dir[0];
                                int nextCol = curr[1] + dir[1];

                                ! // For each cell with the value equal to empty land value
                                ! // add distance and decrement the cell value by 1.
                                if (nextRow >= 0 && nextRow < rows &&
                                    nextCol >= 0 && nextCol < cols &&
                                    grid[nextRow][nextCol] == emptyLandValue) {
                                    grid[nextRow][nextCol]--;
                                    total[nextRow][nextCol] += steps;

                                    q.offer(new int[]{ nextRow, nextCol });
                                    minDist = Math.min(minDist, total[nextRow][nextCol]);
                                }
                            }
                        }
                    }
                    ! // Decrement empty land value to be searched in next iteration.
                    emptyLandValue--;
                }
            }
        }
        return minDist == Integer.MAX_VALUE ? -1 : minDist;
    }
}

"""

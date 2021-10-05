"""
https://leetcode.com/problems/dungeon-game/

"""


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        rows, cols = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * cols for _ in range(rows)]

        def get_min_health(currCell, nextRow, nextCol):
            # ! currCell, current cell value
            # ! nextRow, the structrue is reversed, the next row here denotes the row upper
            # ! nextCol, the next col is the column to the current column

            # ! boundary check
            if nextRow >= rows or nextCol >= cols:
                return float('inf')
            # ! update value based on current situation
            nextCell = dp[nextRow][nextCol]
            # ! hero needs at least 1 point to survive
            return max(1, nextCell - currCell)

        # ! staring from the right bottom element
        # ! the double iteration is a procedure that updates values of dp matrix
        for row in reversed(range(rows)):
            for col in reversed(range(cols)):
                currCell = dungeon[row][col]
                # ! from left
                right_health = get_min_health(currCell, row, col+1)
                # ! from up
                down_health = get_min_health(currCell, row+1, col)
                # ! update health value
                next_health = min(right_health, down_health)
                # ! initialized value of health matrix is "inf"
                if next_health != float('inf'):
                    min_health = next_health
                else:
                    # ! if current cell value is not inf and current cell value is >=0, which means there is no daemon in the cell.
                    # ! if current cell is smaller than 0, which means there is a daemon and then set the new min health as 1-currCell, because in order to overcome the daemon, we need one more extra blood.
                    min_health = 1 if currCell >= 0 else (1 - currCell)
                # ! update dp matrix
                dp[row][col] = min_health

        return dp[0][0]


"""
Starting from the right bottom connor to the left top connor


"""


class Solution:
    def calculateMinimumHP(self, dungeon):
        height = len(dungeon)
        width = len(dungeon[0])
        # ! the minumum hp that warrior needs
        # ! since we are going to get the minimum values, so it is more appropriate to initialize the values with inf(positive)
        dp = [[float('inf') for i in range(width+1)] for j in range(height+1)]

        # ! base case, to reach the princess, at least we need 1 blood
        # * 这个表示到达右下角P处之后，继续往右，或者往下走一格（越界，可以认为每个格子是0）之后最少HP=1（还活着），
        # * 这也就表示在P点也活着。hp[m-1][n-1] 就可以根据 hp[m][n-1] / hp[m][n-1] / grid[m-1][n-1] 算出来了。
        # * 如果grid[m-1][n-1]是>=0，那么hp[m-1][n-1]就等于min(hp[m][n-1], hp[m][n-1]) = min(1,1) = 1。
        dp[height-1][width] = 1
        dp[height][width-1] = 1

        for row in range(height-1, -1, -1):
            for col in range(width-1, -1, -1):
                # ! get the minimum from right cell or down cell, then minus the value in dungeon, the current cell.
                # ! reason of using minus: we using dp to get the minimum hp value.
                # ! If the cell contains a daemon, then using minus is adding the blood(-- => +) we need to overcome the current daemon
                # ! If the cell contains med(-+ => -), then we minus it.
                fromPreviousCells = min(dp[row+1][col], dp[row][col+1])
                afterMedOrDaemon = fromPreviousCells - dungeon[row][col]
                # ! using max to get the maximum between these two values
                # ! we have set two values
                # !      dp[height-1][width] = 1
                # !      dp[height][width-1] = 1
                # ! 1 avoid the two cases influencesS at the beginning
                # ! 2 avoid the negative cases of currentCell value
                dp[row][col] = max(1, afterMedOrDaemon)

        return dp[0][0]

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
        # ! 
        def get_min_health(currCell, nextRow, nextCol):
            if nextRow >= rows or nextCol >= cols:
                return float('inf')
            nextCell = dp[nextRow][nextCol]
            # hero needs at least 1 point to survive
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
                # ! update previous health value
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
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        
        score = 0
        
        for row in range(height):
            for col in range(width):
                if grid[row][col]:
                    score = max(score, self.helper(grid,height,width,row,col))
    
        return score
        
    def helper(self,grid,height,width,row,col):
        
        if row<0 or row>=height:
            return 0
        if col<0 or col>=width:
            return 0
        
        if grid[row][col]==0:
            return 0
        
        grid[row][col]=0
        
        return 1+self.helper(grid,height,width,row+1,col)+\
                self.helper(grid,height,width,row-1,col)+\
                self.helper(grid,height,width,row,col+1)+\
                self.helper(grid,height,width,row,col-1)
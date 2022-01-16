class Solution(object):          
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row = len(grid)
        column = len(grid[0])
        result = 0
        
        if not grid or len(grid) == 0:
            return
        
        for i in range(row):
            for j in range(column):
                if grid[i][j] == '1':
                    result += 1
                    self.dfs(grid,i,j,row,column)
        return result
        
    def dfs(self,grid,x,y,row,column):
        if x<0 or y<0 or x>=row or y>= column or grid[x][y]=='0':
            return
        grid[x][y] = '0'
        self.dfs(grid,x-1,y,row,column)
        self.dfs(grid,x+1,y,row,column)
        self.dfs(grid,x,y-1,row,column)
        self.dfs(grid,x,y+1,row,column)

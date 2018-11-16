class Solution:
    def __init__(self):
        self.visited = set()
        self.grid = None
        self.count = 0
        
    def dfs(self, start, isRecursive=True):
        row = start[0]
        col = start[1]
        if start in self.visited:
            return
        if 0 <= row and row < len(self.grid) and 0 <= col and col < len(self.grid[0])\
            and self.grid[row][col] == "1":
            self.visited.add(start)
            if not isRecursive:
                self.count += 1
            # top
            self.dfs((start[0]-1,start[1]))
            # right
            self.dfs((start[0],start[1]+1))
            # bottom
            self.dfs((start[0]+1,start[1]))
            # left
            self.dfs((start[0],start[1]-1))

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.grid = grid
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                self.dfs((row, col), False)
        return self.count

inp =[["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]]
s = Solution()
print(s.numIslands(inp))

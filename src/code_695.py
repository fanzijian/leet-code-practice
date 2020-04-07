class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(x, y):
            tmp = set([(x,y)])
            size = 0
            while tmp:
                i,j = tmp.pop()
                self.is_visited.add((i,j))
                if grid[i][j] == 1:
                    size += 1
                    if i < m - 1 and (i+1, j) not in self.is_visited:
                        tmp.add((i+1,j))
                    if j < n - 1 and (i, j+1) not in self.is_visited:
                        tmp.add((i,j+1))
                    if i > 0 and (i-1, j) not in self.is_visited:
                        tmp.add((i-1,j))
                    if j > 0 and (i,j-1) not in self.is_visited:
                        tmp.add((i,j-1))
            return size

        if not grid:
            return 0
        m  = len(grid)
        n = len(grid[0])
        max_size = 0
        self.is_visited = set()
        for i in xrange(0, m, 1):
            for j in xrange(0, n, 1):
                if (i, j) in self.is_visited or grid[i][j] == 0:
                    self.is_visited.add((i,j))
                    continue
                if grid[i][j] == 1:
                    size = dfs(i, j)
                    print [i, j], size
                    max_size = max(size, max_size)
        return max_size


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

obj = Solution()
print  obj.maxAreaOfIsland(grid)


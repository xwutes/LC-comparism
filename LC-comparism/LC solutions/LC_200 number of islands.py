# LC_200 number of islands

from sklearn import neighbors

import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        num_island = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == "1":
                    num_island += 1
                    grid[i][j] == "0"
                    neighbors = collections.deque((i,j))
                    while neighbors:
                        i,j = neighbors.popleft()
                        for x, y in [(i-1,j),(i+1,j),(i,j-1),(i, j+1)]:
                            if 0<= x < nr and 0<= y < nc and grid[x][y] == "1":
                                neighbors.append((x,y))
                                grid[x][y] == "0"
        return num_island



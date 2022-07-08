# LC_994 Rotting Oranges
import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        Q = collections.deque()
        fresh = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 2:  
                    Q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        time = 0                                             
        while Q and fresh > 0:
            for e in range(len(Q)):         # this will loops according to element amout in que
                i, j = Q.popleft()          # using same pattern as treenode traveral, don't use pop
                for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if 0 <= x < h and 0 <= y < w and grid[x][y] == 1:
                        grid[x][y] = 2
                        Q.append((x,y))     # if using pop then there will be missing elements that ought to be traversed
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1
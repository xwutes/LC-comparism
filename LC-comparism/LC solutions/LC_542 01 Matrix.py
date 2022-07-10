# LC_542 01 Matrix

import collections
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j]== 0:
                    q.append((i,j))
                else:                           # mark the "#" first and then save searching time.
                    mat[i][j] = "#"             # there is a key for saving time is to mark the target value
        while q:
            i, j = q.popleft()
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and mat[x][y] == "#":          # in this line there won't be redundance
                    mat[x][y] = mat[i][j] + 1
                    q.append((x, y))
                    
        
        return mat
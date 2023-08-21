from collections import deque

class Solution(object):
    def numIslands(self, grid):
        
        m = len(grid)
        n = len(grid[0])
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0 ,-1 ,1]
        
        visited = [[0 for _ in range(n)] for _ in range(m)]
        
        que = deque()
        answer = 0
        
        def bfs(i,j):
            
            que.append((i,j))
            visited[i][j] == 1
                        
            while que:
                
                x, y = que.popleft()
                
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                
                    if nx < 0 or ny < 0 or nx >= m or ny >= n:
                        continue
        
                    if visited[nx][ny] == 0 and grid[nx][ny] == "1":
                        que.append((nx,ny))
                        visited[nx][ny] = 1
                    
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    bfs(i,j)
                    answer += 1
        
        return answer
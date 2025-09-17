from collections import deque

def solution(board):
    n = len(board) # 5
    m = len(board[0]) # 7
    
    # 시작 위치와 도착위치 찾기
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R': # board[0][6]
                start = (i,j)
            elif board[i][j] == 'G': # board[1][3]
                goal = (i,j)
    
    directions = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우
    visited = [[False] * m for _ in range(n)] # 7 x 5
    queue = deque()
    queue.append((start[0], start[1], 0)) # x,y,이동횟수
    visited[start[0]][start[1]] = True
    
    while queue: 
        x, y, count = queue.popleft() # 0 6 0
        
        if (x,y) == goal:
            return count
        
        for dx, dy in directions:
            nx, ny = x, y
            # 미끄러지기
            while True:
                tx = nx + dx
                ty = ny + dy
                if 0 <= tx < n and 0 <= ty < m and board[tx][ty] != 'D':
                    nx, ny = tx, ty
                else:
                    break
                    
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, count + 1))
            
            #print(queue)
    return -1
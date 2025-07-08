# BFS 문제 - 최단경로 보장
from collections import deque

def solution(x, y, n):
    queue = deque()
    queue.append((x , 0)) # queue에 현재 숫자와 연산횟수 입력
    
    visited = set() # 중복 방지
    
    while queue:
        current, count = queue.popleft()
        
        # 종료 조건
        if current == y:
            return count
        
        # visited 처리
        if current in visited:
            continue
        visited.add(current)
        
        for next_num in (current + n, current * 2, current * 3):
            if next_num <= y:
                queue.append((next_num, count + 1))

    return -1
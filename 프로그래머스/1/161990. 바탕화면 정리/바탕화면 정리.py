def solution(wallpaper):

    
    # 최소 행,열 (lu, luy)
    # 최대 행,열 (rdx + 1, rdy +1)

    # 행열 초기화
    lux, luy = float('inf'), float('inf')
    rdx, rdy = 0, 0
    
    for i in range(len(wallpaper)): # 첫 예시 range (3) -> 0 .. 1 .. 2 ----> 따라서 행 -> 세로 인덱스
        for j in range(len(wallpaper[0])): # 열 -> 가로 인덱스 ---> len(wallpaper[0])는 5 
            if wallpaper[i][j] == '#':
                lux = min(lux, i) # 행
                luy = min(luy, j) # 열
                rdx = max(rdx, i + 1) 
                rdy = max(rdy, j + 1)
    
    answer = [lux, luy, rdx, rdy]
    
    return answer
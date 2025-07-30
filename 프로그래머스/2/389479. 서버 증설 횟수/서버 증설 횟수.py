"""
시뮬 + 큐 사용
if +m명 늘어날때마다 -> server 1대

n x m < player < (n + 1) x m  => server += n

server = time + k

m : 증가되는 인원 수
k : 운영되는 시간
player[i] = i시각 부터 i+1 시각까지 게임 이용자 수

-> 모든 시간을 감당할 수 있는 최소 증설 횟수를 구하는 것
-> 증설횟수 answer += 
-> m이 3일 경우 3의 배수만큼 증설된 횟수 1씩 증가? player[i] // m -> server += 1

need_server = ceil(palyer[i] / m) -> 올림 함수 필요! 
ex) player 7명일 경우 -> 3대 필요 but player[i] // m 으로 진행할 경우 2대의 서버만 구축됨

active_server 랑 비교

게임 이용자 수를 통해 필요한 서버 수 계산
-> 현재 운영중인 서버와 필요한 서버 수 비교
-> 운영중인 서버가 필요한 서버에 비해 부족할 경우 증설
"""

import math
from collections import deque

def solution(players, m, k):
    answer = 0 # 총 증설 횟수 누적값 필요
    running_server = deque()
    
    for t in range(24): # 0~23 시간 순회
        # 현재 위치한 t 시간에 종료되는 서버 제거
        while running_server and running_server[0] <= t:
            running_server.popleft()
            #print(f"운영중인 서버 : {running_server}")
        
        #print(f"t시간대 : {t} -> 이용자 수 :{players[t]}")
        need_server = players[t] // m # 현재 t시간에 필요한 서버 계산
        #print(f"필요한 서버 : {need_server}")
        
        lack_of_server = need_server - len(running_server)
        #print(f"부족한 서버 : {lack_of_server}")
        #print()
        if lack_of_server > 0:
            answer += lack_of_server
            for _ in range(lack_of_server):
                running_server.append(t + k)
    return answer
"""
시간 -> 분 단위로 변경
종료 시간에는 + 10M
입실 시간 기준으로 정렬하기

입실 시간 순 정렬
["14:10", "19:20"], 
["14:20", "15:20"],
["15:00", "17:00"], 
["16:40", "18:20"], 
["18:20", "21:20"]
입력 배열 루프 -> 14:10 무조건 신규 객실 1번 필요!!! -> 14:20 이랑 1번 손님의 종료시간이 19:20 비교
-> 가장 이른 퇴실시간 + 10M(19:30) > 다음 손님 입실시간 (14:20) 이기 때문에  => 신규 객실 2번 필요!!!
-> 3번쨰 손님 마찬가지로 가장 이른 퇴실시간 + 10M(15:30) > 다음 손님 입실 시간(15:00) => 신규 객실 3번 필요!!!
-> 4번째 손님 가장 이른 퇴실시간 + 10M (15:30) < 다음 손님 입실 (16:40) => 객실 2번 사용

최소 힙 = ["18:30" "19:30", "21:20"]
"""
import heapq
def time_to_minutes(t):
    hour, minute = map(int, t.split(":"))
    
    return hour * 60 + minute

def solution(book_time):
    book_time.sort()
    times = [] # 힙으로 사용
    
    for start, end in book_time:
        start_minute = time_to_minutes(start)
        end_minute = time_to_minutes(end) + 10
        times.append((start_minute, end_minute))
    # [(850, 1170), (860, 930), (900, 1030), (1000, 1110), (1100, 1290)]
    
    heap = []
    
    for start, end in times:
        if heap and heap[0] <= start:
            heapq.heappop(heap)
        heapq.heappush(heap, end)
    
    answer = len(heap)
    return answer

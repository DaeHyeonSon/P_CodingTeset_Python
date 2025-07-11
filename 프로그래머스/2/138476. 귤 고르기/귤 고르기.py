from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)

    counter_list = sorted(counter.values(),reverse=True) # counter.values()는 {3: 2, 2: 2, 5: 2, 1: 1, 4: 1} 여기서 value값들, 그리고 내림차순 진행
       
    
    answer = 0
    total = 0
    for count in counter_list:
        total += count
        answer += 1
        if total >= k:
            break    
    
    return answer
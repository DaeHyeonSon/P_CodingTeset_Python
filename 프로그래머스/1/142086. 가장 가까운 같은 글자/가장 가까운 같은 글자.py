def solution(s):
    answer = []
    last_seen = {}
    
    for i, ch in enumerate(s):
        if ch not in last_seen:
            answer.append(-1)
        else:
            result = i - last_seen[ch]
            answer.append(result)
        last_seen[ch] = i
        
    return answer
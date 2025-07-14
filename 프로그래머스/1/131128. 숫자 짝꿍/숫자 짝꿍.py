from collections import Counter

def solution(X, Y):
    
    x_counter = Counter(X)
    y_counter = Counter(Y)
    
    answer = []
    for d in '9876543210':
        if d in x_counter and d in y_counter:
            count = min(x_counter[d], y_counter[d])
            answer.append(d * count)
    
    if not answer:
        return "-1"
    
    answer = "".join(answer)
    
    if answer[0] == "0":
        return "0"
        
    return answer
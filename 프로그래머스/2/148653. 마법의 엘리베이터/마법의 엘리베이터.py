# 각 자릿수 
# 일단 일의 자리가 0~4 일 경우에는 -1씩 내려감, 6~9 일 경우에는 +1씩 올라감, 5는 앞자리가 5 이상일 경우 올림
# 2 5 5 4 => 4 -4내림, 5 -> 5 +5올림, 올림 후 6 -> +4 올림, 올림 후 2+1 -> 3
def solution(storey):
    answer = 0
    
    while storey > 0:
        digit = storey % 10
        next_digit = (storey // 10) % 10 # 다음 자리
        
        if digit > 5 or (digit == 5 and next_digit >= 5): # 올림이 이득
            answer += 10 - digit # storey = 16일때 answer = 4
            storey += 10 # 26
        else: # 내림이 이득
            answer += digit
            
        storey //= 10
            
    return answer
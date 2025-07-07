def solution(a, b, n):
    answer = 0
    
    while(n >= a):
        exchange = n // a
        new_coke = exchange * b
        answer += new_coke
        n = n % a + new_coke
    
    return answer
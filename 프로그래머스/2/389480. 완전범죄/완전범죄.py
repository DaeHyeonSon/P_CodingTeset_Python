def solution(info, n, m):
    answer = 0
    INF = float('inf')
    dp = [[INF] * m for _ in range(len(info) +1)] # 4 x 4 
    dp[0][0] = 0
    
    
    for i in range(len(info)):
        a_trace, b_trace = info[i] # 1 2, 2 3, 2 1
        for b in range(m):
            if dp[i][b] == info: continue
            
            new_a = dp[i][b] + a_trace
            if new_a < n:
                dp[i+1][b] = min(dp[i+1][b], new_a)
            
            new_b = b + b_trace
            if new_b < m:
                dp[i+1][new_b] = min(dp[i+1][new_b], dp[i][b])
    
    result = min(dp[len(info)])
    return result if result != INF else -1
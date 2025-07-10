def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x: (x[col - 1], -x[0]))
    
    answer = 0
    
    for i in range(row_begin, row_end + 1):
        row = data[i - 1]
        S_i = sum(value % i for value in row)
        answer ^= S_i
    
    return answer
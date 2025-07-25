def solution(sequence, k):
    
    n = len(sequence)
    left = right = 0
    total = sequence[0] # 현재 배열 시퀀스의 합 = 합
    answer = [0, n - 1]
    
    while right < n:
        if total < k:
            right += 1
            if right < n: # 시퀀스 길이보다 길어지면 안되니깐 제약사항 추가
                total += sequence[right]
        
        elif total > k:
            total -= sequence[left]
            left += 1
        
        else: # total == k:
            if (right - left) < (answer[1] - answer[0]):
                answer = [left, right]
                
            total -= sequence[left]
            left += 1
        
    return answer
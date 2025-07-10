def solution(k, m, score):
    # 1. score 먼저 정렬 -> 내림차순으로 큰수부터 나열되는 식
    score.sort(reverse=True) # 	[3, 3, 2, 2, 1, 1, 1]

    answer = 0
    # 2. m개씩 잘라서 묶는다 (나머지는 버림)
    for i in range(len(score) // m):
        # 3. 가장 낮은 점수 x m 진행을 위한 과정
        box = score[i * m:(i + 1) * m] # -> score[0:4] --> [3,3,2,2]
        min_score = min(box) # 최솟값 2
        answer += min_score * m
    
    return answer
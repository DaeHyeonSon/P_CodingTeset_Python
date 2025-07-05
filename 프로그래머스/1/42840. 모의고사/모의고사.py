def solution(answers):
    # 1. 세 수험생의 패턴 정의
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 2. 세 수험생의 정답 계수
    score1, score2, score3 = 0, 0, 0
    
    for i in range(len(answers)):
        if answers[i] == p1[i % len(p1)]:
            score1 += 1
        if answers[i] == p2[i % len(p2)]:
            score2 += 1
        if answers[i] == p3[i % len(p3)]:
            score3 += 1
            
    # 3. 최대 점수 max를 통해 리스트 형태로 저장
    max_score = max(score1, score2, score3)
    
    # 4. 최대 점수를 받은 인원 오름차순으로 출력
    result = []
    if score1 == max_score:
        result.append(1)
    if score2 == max_score:
        result.append(2)
    if score3 == max_score:
        result.append(3)
        
    return result
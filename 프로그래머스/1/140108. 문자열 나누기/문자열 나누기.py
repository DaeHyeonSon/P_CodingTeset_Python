def solution(s):
    result = 0
    x = ''
    x_count = 0
    other_count = 0
    
    # 첫 문자일 경우 첫 글자 설정
    for i, ch in enumerate(s):
        if x_count == 0:
            x = ch
            x_count = 1
            other_count = 0
        else:
            if ch == x:
                x_count += 1
            else:
                other_count += 1
        
        if x_count == other_count:
            result += 1
            x_count = 0 # result에 값 추가되면 x_count 값 초기화
            other_count = 0
        
    # 반복문을 다 돌고도 남아있는 경우 대비 Like  입출력 예시 2 -> 마지막 a 남음
    if x_count != 0 or other_count != 0:
        result += 1
    
    return result
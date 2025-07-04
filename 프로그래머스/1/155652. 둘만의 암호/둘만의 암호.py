def solution(s, skip, index):
    
    # skip word는 set함수 사용하여 집합
    skip_set = set(skip)
    
    # 사용 가능한 알파벳 리스트로 변환
    available = []
    for i in range(ord('a'), ord('z') + 1):  # <- a ~ z (97 ~ 122)까지
        ch = chr(i)
        if ch not in skip_set:
            available.append(ch)
    
    print(available) # ['a', 'c',..., 'y', 'z']
    
    answer = ""
    
    for ch in s: # <- 'a' 'u' 'k'...
        idx = available.index(ch) # ex) available 리스트 안에서 index(a) 몇번째인지 확인 !!!! 한마디로 현재 문자의 위치를 알려주는 느낌
        new_char = available[(idx + index) % len(available)]
        print(f"현재 문자: {ch}, 위치: {idx}, len길이: {len(available)}, 변환 후 위치: {(idx + index) % len(available)}")
        print(new_char)
        answer += new_char
        
    
    
    return answer
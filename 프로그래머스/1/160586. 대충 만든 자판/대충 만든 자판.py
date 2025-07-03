def solution(keymap, targets):
    # 각 문자별 최소 누름 횟수 저장할 dict
    keymapdict = {}
    
    for key in keymap:
        for i, char in enumerate(key): # i는 인덱스로서 누른횟수는 -> i+1
            if char not in keymapdict:
                keymapdict[char] = i + 1
            else:
                keymapdict[char] = min(keymapdict[char], i + 1)
    print("문자별 최소 누름 횟수 : ", keymapdict)
    
    answer = []
    
    for word in targets:
        total = 0
        for char in word:
            if char in keymapdict:
                total += keymapdict[char]
            else:
                total = -1
                break
        answer.append(total)
        
    return answer
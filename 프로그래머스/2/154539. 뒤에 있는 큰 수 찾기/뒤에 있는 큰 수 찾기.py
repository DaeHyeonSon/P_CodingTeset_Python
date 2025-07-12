# 문제 이해: 각 배열에 들어오는 자신의 숫자보다 큰 수 출력. if 없다면 -1
# brute force로 푼 결과 시간 초과!
#def solution(numbers):
#    answer = [-1] * len(numbers)
    
#    for i in range(len(numbers)):
#        for j in range(i+1, len(numbers)):
#            if numbers[i] < numbers[j]:
#                answer[i] = numbers[j]
#                break
#    
#    return answer

## 따라서 stack 사용 LIFO 구조
def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for i in range(len(numbers) -1, -1, -1): # 3~0까지 감소하며 역순 탐색
        while stack and stack[-1] <= numbers[i]: # stack이 비어있지 않는 동안
            stack.pop()
        if stack:
            answer[i] = stack[-1]
            
        stack.append(numbers[i])
    
    return answer
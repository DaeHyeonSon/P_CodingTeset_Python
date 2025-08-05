'''
# 1 ~ n 개 박스

1. order는 리스트 순회
2. 보조 컨테이너 -> stack
3. 컨테이너벨트 1~n 까지 while로 순회

'''

def solution(order):
    stack = []
    order_idx = 0
    box = 1 # 컨테이너벨트에서 꺼낼 상자 번호
    n = len(order)
    
    # 컨테이너벨트 1~n 까지 진행
    while box <= n:
        
        # 만약 꺼내야할 box가 order[order_idx]와 같을 경우 => 바로 택배 실음
        if box == order[order_idx]:
            order_idx += 1
            box += 1 # 계속 증가 시켜줘야 함
        
        # 보조컨테이너 벨트에서 실을 수 있는 경우 | stack top 젤 위에 있는게 order과 맞으면 pop()
        elif stack and stack[-1] == order[order_idx]:
            stack.pop()
            order_idx += 1
        
        # 그 외 아닐 경우 보조벨트에 보관
        else:
            stack.append(box)
            box += 1 # 계속 증가 시켜줘야 함
    
    # box는 끝났지만 stack에 남아있는것을 확인해야 함! 그래서 한번 더 stack 확인 필요
    while stack and stack[-1] == order[order_idx]:
        stack.pop()
        order_idx += 1
    
    
    return order_idx
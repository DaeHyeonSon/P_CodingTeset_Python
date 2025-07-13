def solution(n, w, num):
    # 상자들의 좌표를 저장 (번호 → (row, col))
    positions = {}

    for i in range(n):
        row = i // w
        col = i % w

        # 짝수 row는 왼→오, 홀수 row는 오→왼
        if row % 2 == 0:
            real_col = col
        else:
            real_col = w - 1 - col

        positions[i + 1] = (row, real_col)

    # 찾을 상자의 좌표
    target_row, target_col = positions[num]

    # 위에 있는 상자 수
    count = 0
    for box_num, (row, col) in positions.items():
        if col == target_col and row > target_row:
            count += 1

    return count + 1  # 자기 자신도 포함
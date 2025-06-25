def solution(friends, gifts):
    n = len(friends)
    name_to_index = {name: i for i, name in enumerate(friends)}

    gift_matrix = [[0] * n for _ in range(n)]
    given = [0] * n
    received = [0] * n

    for gift in gifts:
        giver, receiver = gift.split()
        gi = name_to_index[giver]
        ri = name_to_index[receiver]
        gift_matrix[gi][ri] += 1
        given[gi] += 1
        received[ri] += 1

    gift_score = [given[i] - received[i] for i in range(n)]
    next_month = [0] * n

    for i in range(n):
        for j in range(i + 1, n):  # 쌍은 한 번만 비교
            give_i_to_j = gift_matrix[i][j]
            give_j_to_i = gift_matrix[j][i]

            if give_i_to_j > give_j_to_i:
                next_month[i] += 1
            elif give_i_to_j < give_j_to_i:
                next_month[j] += 1
            else:
                if gift_score[i] > gift_score[j]:
                    next_month[i] += 1
                elif gift_score[i] < gift_score[j]:
                    next_month[j] += 1

    return max(next_month)
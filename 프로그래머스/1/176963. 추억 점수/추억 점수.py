def solution(name, yearning, photo):
    name_to_score = dict(zip(name, yearning))
    answer = []
    for p in photo:
        score = 0
        for person in p:
            score += name_to_score.get(person, 0)
        answer.append(score)
    return answer
def solution(k, score):
    answer = []
    klist = []
    for i in score:
        klist.append(i)
        if len(klist) > k:
            klist.remove(min(klist))
        answer.append(min(klist))
    return answer
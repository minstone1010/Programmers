def solution(k, score):
    answer = []
    klist = []
    for i in score:
        klist.append(i)
        klist.sort(reverse=True)
        if len(klist) > k:
            klist.pop()
        answer.append(klist[len(klist)-1])
    return answer
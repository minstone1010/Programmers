def solution(n):
    n = list(n)
    answer = []
    for i in range(len(n)):
        answer[len(n)-i] = n[i]
    return answer
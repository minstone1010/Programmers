def solution(n, m):
    answer = []
    nlist = []
    mlist = []
    for i in range(1, n+1):
        if n % i == 0:
            nlist.append(i)
    for i in range(1, m+1):
        if m % i == 0:
            mlist.append(i)
            
    answer.append(max(list(set(nlist) & set(mlist))))
    
    if m % n == 0 or n % m == 0:
        answer.append(max(n, m))
    else:
        answer.append(n*m//answer[0])
    return answer
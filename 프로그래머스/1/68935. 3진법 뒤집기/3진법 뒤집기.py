def solution(n):
    answer = 0
    num = ""
    while n > 0:
        num = str(n % 3) + num
        n //= 3
    
    for i in range(len(num)):
        answer += (3**i) * int(num[i])
    return answer
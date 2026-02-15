def solution(n):
    n = list(str(n))
    answer = 0
    
    for i in range(len(n)):
        answer += int(n[i])

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('str(answer)')

    return answer
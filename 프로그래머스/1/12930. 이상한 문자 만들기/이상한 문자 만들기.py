def solution(s):
    answer = ''
    n = 0
    for i in s:
        if i == " ":
            answer += " "
            n = 0
        else:
            if n % 2 == 0:
                answer += i.upper()
            else:
                answer += i.lower()
            n += 1
    return answer
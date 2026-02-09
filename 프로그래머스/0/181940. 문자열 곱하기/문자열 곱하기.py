def solution(my_string, k):
    answer = []
    
    for i in range(k):
        answer.append(my_string)
        
    answer = ''.join(answer)
    return answer
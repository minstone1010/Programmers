def solution(food):
    answer = ''
    half = []
    for i in range(len(food)):
        half.append(food[i]//2)
        
    for i in range(1, len(half)):
            for j in range(half[i]):
                answer += str(i)
                
    answer += "0"
    
    for i in range(len(half)-1,0,-1):
            for j in range(half[i]):
                answer += str(i)
    return answer
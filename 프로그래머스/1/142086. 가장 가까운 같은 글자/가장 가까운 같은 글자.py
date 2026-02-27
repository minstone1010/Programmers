
def solution(s):
    answer = []
    
    for i in range(len(s)):
        found = False
        
        for j in range(i-1, -1, -1): 
            if s[j] == s[i]:
                answer.append(i - j)
                found = True
                break
        
        if not found:
            answer.append(-1)
    
    return answer
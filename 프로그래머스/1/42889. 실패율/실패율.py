def solution(N, stages):
    answer = []
    total = len(stages)
    for i in range(1, N+1):
        count =stages.count(i) 
        
        if total == 0:
            fail = 0
        else:
            fail = count/total
        
        answer.append((i,fail))
        
        total -= count
        stages = [x for x in stages if x != i]
    
    answer.sort(key=lambda x: (-x[1], x[0]))
    answer = [i for i, _ in answer]
    return answer

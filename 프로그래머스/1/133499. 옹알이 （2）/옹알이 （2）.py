def solution(babbling):
    answer = 0
    baby = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        prev = ""
        
        while True:
            matched = False
            
            for b in baby:
                if word.startswith(b) and prev != b:
                    word = word[len(b):]
                    prev = b
                    matched = True
                    break
            
            if not matched:
                break
        
        if word == "":
            answer += 1
    
    return answer
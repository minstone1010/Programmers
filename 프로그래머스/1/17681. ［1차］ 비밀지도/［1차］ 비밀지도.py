def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        wall = arr1[i] | arr2[i]
        row = format(wall, "b").zfill(n)
        row = row.replace("1", "#")
        row = row.replace("0", " ")
        
        answer.append(row)
    return answer
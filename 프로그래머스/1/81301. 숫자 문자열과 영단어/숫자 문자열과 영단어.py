def solution(s):
    answer = 0
    num_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
}
    num = ""
    result = ""
    for i in s:
        if i.isdigit():
            result += i
        else:
            num += i
            if num in num_dict:
                result += num_dict[num]
                num = ""
            
    answer = int(result)
    return answer
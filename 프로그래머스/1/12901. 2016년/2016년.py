import datetime

def solution(a, b):
    answer = ''
    days = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    
    date = datetime.date(2016, a, b)
    answer = days[date.weekday()]
    return answer
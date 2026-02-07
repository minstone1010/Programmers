str = list(input())

for i in range(len(str)):
    if str[i].isupper():
        str[i] = str[i].lower()
    else:
        str[i] = str[i].upper()
        
str = ''.join(str)
print(str)
    
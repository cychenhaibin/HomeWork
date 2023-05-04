def strcat(str1,char1):
    str2 = ''
    for i in str1:
        if i == ' ':
            str2 += char1
        else:
            str2 += i
    return str2

str1 = str(input())
char1 = str(input())

str2 = strcat(str1,char1)
print(str2)
mi_words = str(input())
sum1 = 0
for i in mi_words:
    sum1 += ord(i)

mi_pian = sum1%26

with open('mayun.txt','r',encoding='utf-8')as f:
    str_content = f.read()

count_upper = 0
count_lower = 0
count_space = 0
count_num = 0
count_others = 0


temp_str_content = str_content.replace('\n',' ')

count_words = len(temp_str_content.split(' '))

for i in str_content:
    if i.isupper():
        count_upper +=1
    elif i.islower():
        count_lower += 1
    elif i.isdigit():
        count_num += 1
    elif i.isspace():
        count_space += 1
    else:
        count_others += 1

mi_str_content = ''

for i in str_content:
    if (i >= 'a' and i <= 'z'):
        temp = (ord(i) - 97 + int(mi_pian)) % 26 + 97

    elif (i >= 'A' and i <= 'Z'):
        temp = (ord(i) - 65 + int(mi_pian)) % 26 + 65

    else:
        temp = ord(i)

    mi_str_content += chr(temp)

with open('mayun.txt','a',encoding='utf-8')as file:
    file.write(mi_str_content)

print(count_upper,count_lower,count_num,count_space,count_others)
print(str(count_words) + ' words in all')
print(mi_pian)
print(mi_str_content)

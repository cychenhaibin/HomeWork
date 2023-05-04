
with open('mayun.txt', 'r') as f:
    data = f.read()

# 统计字符数量
upper = 0
lower = 0
digit = 0
space = 0
others = 0
for char in data:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
    elif char.isdigit():
        digit += 1
    elif char.isspace():
        space += 1
    else:
        others += 1

print('大写字母数量：', upper)
print('小写字母数量：', lower)
print('数字数量：', digit)
print('空白字符数量：', space)
print('其他字符数量：', others)

# 统计单词数量
data = data.replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace(';', '').replace(':', '')
words = data.split()
print('单词数量：', len(words))

# 恺撒加密
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
secret_word = input('请输入秘密单词：')
while secret_word not in days:
    secret_word = input('请重新输入秘密单词，必须是以下单词之一：' + ', '.join(days) + '\n')

shift = sum(ord(char) for char in secret_word) % 26
encrypted_data = ''
for char in data:
    if char.isupper():
        encrypted_data += chr((ord(char) - 65 + shift) % 26 + 65)
    elif char.islower():
        encrypted_data += chr((ord(char) - 97 + shift) % 26 + 97)
    else:
        encrypted_data += char

print('加密结果如下：\n' + encrypted_data)


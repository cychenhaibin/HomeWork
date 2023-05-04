def getText():
    txt = open("hamlet.txt","r").read()#打开文本
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch," ")
    
    return txt
n=eval(input())
hamletTxt = getText()
counts = {}
words= hamletTxt.split()
for word in words:
    counts[word] = counts.get(word,0)+1
items = list(counts.items())#返回元组类型元素的列表
items.sort(key=lambda x:x[1],reverse = True)#倒序 对键值进行排序
for i in range(n):
    word,count = items[i]
    print("{:<10}{:>5}".format(word,count))

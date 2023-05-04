a=input()
str_upper,str_lower,n=0,0,0
for i in a:
    if i.islower():
        str_lower+=1
    elif i.isupper():
        str_upper+=1
    elif i.isdigit():
        n+=1
print(str_upper)
print(str_lower)
print(n)
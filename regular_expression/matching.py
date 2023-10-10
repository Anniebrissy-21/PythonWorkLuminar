from re import *
text="abababcdab"
    # 01234567

matcher=finditer("ab",text)

count=0
#print(matcher)
for m in matcher:
    print(m.start(),m.group())
    count+=1
print(count)






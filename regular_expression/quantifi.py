from re import *
text="aabaabc"

pattern="a?"

matcher=finditer(pattern,text)
for m in matcher:
    print(m.group(),m.start())
text="ABCDA"
#print first recursive character
wc={}
for char in text:
    if char in wc:
        print("first recursive character is",char)
        break
    else:
        wc[char]=1

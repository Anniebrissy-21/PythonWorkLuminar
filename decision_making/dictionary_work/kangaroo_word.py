source_word="decreased"
target_word="dress"
wc={}
#source word count
is_kangaroo=True
for ch in source_word:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1
#target word check

for ch in target_word:  #ch=d
    if ch in wc:             #if ch in wc and wc.get(ch)>0
        current_val=wc[ch]   #exracting the exact current value
        if current_val>0:     
            wc[ch]-=1
        else:
            is_kangaroo=False
            break
print(is_kangaroo)

     



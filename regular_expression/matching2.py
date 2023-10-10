from re import *
text="abicdu$ABC#D7eO9fk_U"
#     0123456789101112
#[0-9]
#pattern="[0-9]" #chk for digit
#pattern="[a-z]"  #chk for lower case alphabets
#pattern="[A-Z]"  #chk for upper case alphabets
#pattern="[a-zA-Z]" #all alphabets
#pattern="[a-zA-Z0-9]" #chk for all alphanumeric characters
#pattern="[^0-9]"  #^except 0-9 all others will print
#pattern="[^A-Za-z0-9]" #only special characters
#pattern="[aeiouAEIOU]" #vowels only
#pattern="[^aeiou]"
pattern="[b-df-hj-np-tv-z]"
#count=0

matcher=finditer(pattern,text)

for m in matcher:
    #if m.group().isalpha():
        print(m.group())
    
    #print(f"location {m.start()} matched group {m.group()}")

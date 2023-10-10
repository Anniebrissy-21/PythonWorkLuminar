#from re import *

#text="aabbcaabdaaa"
    # 01234567891011
#quantifiers

#pattern="a+" #one or more occurence of a
#pattern="a{1,2}"  #zero or more occurence of a
#matcher=finditer(pattern,text)

#for m in matcher:
    #print(m.group(),m.start())

# starts_with an alphabet

#rule="[a-z][a-zA-Z0-9]*"




from re import*

phone=input("Enter the Phone Number:")

rule="\d{10}"   #because phone number is 10 digit

matcher=fullmatch(rule,phone)

if (matcher==None):
    print("invalid")
else:
    print("valid")


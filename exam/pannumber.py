f=open("D:\pythonwork\exam\pans.txt","w")

from re import*


pancrd=input("enter the pancard number:")

rule="[A-Z]{3}[PFCAHT]{1}[A-Z]{1}[0-9]{4}[A-Z]{1}"   

matcher=fullmatch(rule,pancrd)

print("invalid" if matcher==None else "valid")
from re import*

variable=input("Enter the variable:")

rule="[a-zA-Z][a-zA-Z0-9_]*"   #[\w_]*

matcher=fullmatch(rule,variable)

print("valid " if matcher!=None else "invalid")
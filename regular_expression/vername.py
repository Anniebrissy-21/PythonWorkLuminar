#starting with alphabet k,l,m
#scnd_place that must be a digit ad that must be / by 3
#followed by any number of character including 0 num of character

from re import*
variable=input("Enter variable name:")

rule="[klm][369][\w]*"

matcher=fullmatch(rule,variable)

print("in valid" if matcher==None else "valid")
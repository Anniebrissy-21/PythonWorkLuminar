# starting with kl
# two digits
#alpabets min 1 max 2
#4dgits

from re import *

kerela_vehicle_num=input("Enter the vehicle number:")

rule="(KL)-\d{2}-[A-Z]{1,2}-\d{4}"

matcher=fullmatch(rule,kerela_vehicle_num)

print("invalid" if matcher==None else "valid")
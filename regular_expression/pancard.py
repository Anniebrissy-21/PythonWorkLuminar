#first 3 characters must be any upper case alphabet
#in 4th place P,F,C,A,H,T
# in 5th place uppercse random alphabet
#4 dgit
#random 1 uppercase alphabet

from re import*

panid=input("Enter pan card number:")

rule="[A-Z]{3}[PFCAHT]{1}[A-Z]{1}[0-9]{4}[A-Z]{1}"    #\d"{4}

matcher=fullmatch(rule,panid)

print("invalid" if matcher==None else "valid")
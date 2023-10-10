f_read=open("D:/pythonwork/decision_making/exam1/emails.txt")
f_write=open("D:/pythonwork/decision_making/exam1/valid_emails.txt","w")
from re import *
rule1="[\w]+@gmail.com"

for line in f_read:
    word=line.rstrip("\n")
    #print(word)

for w in word:
    matcher=fullmatch(rule1,w)
    if matcher!=None:
        f_write.write(w+"\n")

        
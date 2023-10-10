from re import*

f_read=open("D:/pythonwork/regular_expression/data.txt")

mail_id=[]
contacts=[]
rule1="[\w]+@gmail.com"

rule2="[0-9]{10}"
for line in f_read:
    word=line.rstrip("\n").split(" ")
   # print(word)
    for w in word:
        matcher1=fullmatch(rule1,w)
        matcher2=fullmatch(rule2,w)
        if matcher1!=None:
            mail_id.append(w)
        elif matcher2!=None:
            contacts.append(w)

print(mail_id)
print(contacts)
    
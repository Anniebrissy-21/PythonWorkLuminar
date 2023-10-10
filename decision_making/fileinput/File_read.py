f_read=open("D:/pythonwork/decision_making/fileinput/data.txt")

f_odd=open("D:/pythonwork/decision_making/fileinput/odd.txt","w")
f_even=open("D:/pythonwork/decision_making/fileinput/even.txt","w")

for line in f_read:
    num=int(line.rstrip("\n"))
    if num%2==0:
        f_even.write(str(num)+"\n")
    else:
        f_odd.write(str(num)+"\n")

#[f.write(str(num)+"\n") for num in range(100,600)]


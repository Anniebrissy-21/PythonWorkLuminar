num1=24
num2=18

#print highest factor(hcf)

for num in range (1,(num2+1)):
    if (num1%num==0) and (num2%num==0):
        hcf=num

print("hcf=",hcf)


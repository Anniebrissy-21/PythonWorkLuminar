num1=20
num2=10

for i in range (1,num1+1):
    if num1%i==0 and num2%i==0:
        gcd=i
    lcm=(num1*num2)/gcd
print(lcm)
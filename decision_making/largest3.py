num1=89
num2=29
num3=34

if(num1>num2)and(num1>num3):
    print("num1 is largest")
elif(num2>num1)and(num2>num3):
    print("num2 is largest")
elif(num3>num2)and(num3>num1):
    print("num3 is largest")
elif(num1==num2)and(num2==num3):
    print("all are equal")
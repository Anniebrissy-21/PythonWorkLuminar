def hcf(a,b):
    for i in range (1,b+1):
        if a%i==0 and b%i==0:
            hcf=i
    print(hcf)

a=int(input("enter the value of a="))
b=int(input("enter the value of b="))

hcf(a,b)
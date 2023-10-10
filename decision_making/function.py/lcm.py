def lcm(a,b):
    for i in range (1,a+1):
        if a%i==0 and b%i==0:
            gcd=i
            
        lcm=(a*b)/gcd
    print(lcm)

a=int(input("enter the value of a="))
b=int(input("enter the value of b="))

lcm(a,b)
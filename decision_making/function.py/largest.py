def largest(a,b,c):

    if(a>b)and(a>c):
        print("a is largest")
    elif(b>a)and(b>c):
        print("b is largest")
    else:
        print("c is largest")

a=int(input("Enter value of a="))
b=int(input("Enter value of b="))
c=int(input("Enter value of c="))

largest(a,b,c)
    
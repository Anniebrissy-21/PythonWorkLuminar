name=input("enter the name=>")
num=int(input("enter the number:"))


if num<10:
    for i in range(1,num+1):
        print(name)
        i+=1
else:
    print("too high")
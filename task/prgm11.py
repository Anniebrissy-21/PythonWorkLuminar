num=int(input("Enter number of person wants to invite the party:"))
if num<10:
    for i in range(1,num+1):
        name=input("Enter the name>")
        print(name,"has been invited")
else:
    print("Too many peoples")
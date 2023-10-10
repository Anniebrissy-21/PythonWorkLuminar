
lst=[3,1,5,4]
#find least missing +ve integer

lst.sort()
if(lst[0])!=1:
    print("1 is missing")
else:


    for i in range(0,len(lst)):
        current=lst[i]
        next=lst[i+1]
        diff=next-current
        if diff!=0:
            print(current+1,"is missing")
            break


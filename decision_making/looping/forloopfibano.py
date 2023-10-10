fibanocci_num=100
prev=0
current=1

print(prev)
print(current)
count=1

for i in range (1,fibanocci_num+1):
    fibanocci=prev+current
    prev=current
    current=fibanocci
    count+=1
    if fibanocci<=fibanocci_num:
        print(fibanocci)
    else:
        break

print("count=",count)
    


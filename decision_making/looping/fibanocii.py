# fibanocci series= 0,1,0+1=1,1+1=2,1+2=3,2+3=5,3+5=8,5+8=13,.......

prev=0
current=1
start=1
print(prev)
print(current)

while(start<=3):
    sum=prev+current
    print(sum)
    prev=current  #(prev,current)=(current,sum)
    current=sum
    start=start+1



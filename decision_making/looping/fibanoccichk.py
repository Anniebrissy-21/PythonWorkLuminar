num=int(input("enter the number chk>"))

prev=0
current=1
is_fibo=False
fibo_num=0
start=1
print(prev)
print(current)

while(start<=25):

    fibo_num=prev+current
    if fibo_num==num:
        is_fibo=True
        break
    print(fibo_num)
    prev=current
    current=fibo_num
    start+=1

print(is_fibo)

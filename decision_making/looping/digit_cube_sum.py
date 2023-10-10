num=int(input("enter the number:"))
original=num
sum=0
# op=36 (1**3+2**3+3**3)

#print(),input(),len(),type()

digit_count=len(str(num)) #str will convert number as string

while(num!=0):
    last_digit=num%10
    cube=last_digit**digit_count  # else we can straightly put length of num which is 3(digit_count)
    sum=sum+cube
    num=num//10
print(sum)

if(original==sum):
    print("amstrong")
else:
    print("not amstrong")

            # 3 digit amstrong number
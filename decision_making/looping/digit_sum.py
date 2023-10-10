num=324
sum=0
#op=9(3+2+4=9)

while(num!=0):
    last_digit=num%10
    sum=sum+last_digit
    num=num//10
print(sum)
    
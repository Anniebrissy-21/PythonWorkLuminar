num=234
#o/p=>3,2,4

while(num!=0):#234!-=0
    last_digit=num%10 #234%10=4 23%10=3 2%10=2
    print(last_digit)# 4 3 2
    num=num//10 #234//10=23  23//10=2 2//10=0

num=123
while(num!=0):
    last_digit=num%10
    print(last_digit)
    num=num//10

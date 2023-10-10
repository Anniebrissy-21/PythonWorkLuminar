year=int(input("Enter the year:"))

#case1
#if given year is century year(00) then it is divisible by 400

#case2
# if given year is not a century year then it is divisible by 4

if(year%100==0)and(year%400==0):
    print("Leap year")
elif(year%4==0)and(year%100!=0):  #!=100=>non centuary year
    print("leap year")
else:
    print("not a leap year")
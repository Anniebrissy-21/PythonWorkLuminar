f=open("D:/pythonwork/decision_making/fileinput/year")
#[f.write(str(y)+"\n") for y in range(1830,2024)]

leapyr_write=open("D:/pythonwork/decision_making/fileinput/leap_year.txt","w")
non_leapyr_write=open("D:/pythonwork/decision_making/fileinput/non_leap_year.txt","w")

for line in f:
    years=int(line.rstrip("\n"))
    if(years%100==0)and(years%400==0):
        leapyr_write.write(str(years)+"\n")
    elif(years%4==0)and(years%100!=0):  
        leapyr_write.write(str(years)+"\n")
    else:
        non_leapyr_write.write(str(years)+"\n")
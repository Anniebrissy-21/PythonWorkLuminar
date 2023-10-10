#print all numbers from 1 to 50 if num /by 3 print "a" if num /by 5 "cd" if num / 15 "efg" else print num

start=1
end=50
while(start<=end):
    if(start%15==0):
        print("efg")
    elif(start%5==0):
        print("cd")
    elif(start%3==0):
        print("a")
    else:
        print(start)
    start+=1
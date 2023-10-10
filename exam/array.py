lst=[2,3,4,5]
lst.sort()
lower=0
upper=len(lst)-1  

sum=7
while(lower<upper):
    current_sum=lst[lower]+lst[upper]
    if current_sum==sum:
        print("array",lst[lower],lst[upper])
        lower+=1
    elif current_sum<sum:
        lower+=1
    else:
        upper-=1
lst=[2,3,5,7]
#    0  1 2 3 4
lst.sort()
lower=0
upper=len(lst)-1   #len will be 5 so -1 for 4

sum=8
while(lower<upper):
    current_sum=lst[lower]+lst[upper]
    if current_sum==sum:
        print("pairs",lst[lower],lst[upper])
        lower+=1
    elif current_sum<sum:
        lower+=1
    else:
        upper-=1














#lst=[2,3,5,7]
#sum=8
#sum=7
#for i in range(0,len(lst)-1):
   # for j in range(i+1):
    ##    cu_sum=lst[i]+lst[j]
      #  if cu_sum==sum:
       #     print(lst[i],lst[j])

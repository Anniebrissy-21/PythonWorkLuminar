#binary search

lst=[10,2,13,8,15]
element=15
lst.sort()
lower=0
upper=len(lst)-1

is_present=False
while(lower<=upper):
    mid=(lower+upper)//2
    if element==lst[mid]:
        is_present=True
        break
    elif element<lst[mid]:
        upper=mid-1
    elif element>lst[mid]:
        lower=mid+1
print(is_present)



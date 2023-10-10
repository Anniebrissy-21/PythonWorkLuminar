#Linear Search
#high complexity
lst=[10,2,13,14,5]
element=14
i=0
limit=len(lst)
is_present=False
while(i<limit):
    cur_val=lst[i]
    if cur_val==element:
        is_present=True
        break
    i+=1
print(is_present)


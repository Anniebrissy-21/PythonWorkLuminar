list=[2,1,5,3,6,3,5]
#print duplicate numbers
#duplicate_list=[]
list.sort()
for i in range(0,len(list)-1):
    current=list[i]
    next=list[i+1]
    
    if current==next:   
        #if current not in duplicate_list:
            #duplicate_list.append(current)
#print(duplicate_list)
        print(current,"is duplicate")

    


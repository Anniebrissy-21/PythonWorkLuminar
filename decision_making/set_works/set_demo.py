#set={10,20,30,10,"hello","hai",True}   #without values take as dict
#print(type(set))

#print(set)

#print(set[0])

#lst=[10,2,30,20,30]

#change to set
#st=set(lst)
#print(st)

#st={10,20,30}
#st.add(100)
#print(st)

#st.add("hello")

#print(st)

st1={10,20,30}
st2={11,12,20,24,30}

union_set=st1.union(st2)
print(union_set)

intersection_set=st1.intersection(st2)
print(intersection_set)

difference_set=st1.difference(st2)
print(difference_set)
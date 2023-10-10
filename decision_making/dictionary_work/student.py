student={"roll":100,"name":"ravi","course":"django"}

print(student["course"])

if "total" in student:
    print("present")
else:
    print("not present")

student["grade"]="A+"
print(student["grade"])

print(student)


print(student.get("name"))

print(student.get("salary"))#print as none error will not occur

#print(student["salary"])  #error will occur  
for k in student.keys():  #print all keys one by one
    print(k)
for v in student.values():#print all values 
    print(v)
for k,v in student.items(): #print both keys and values
    print(k,v)

w="is_vaccinated"

if w in student:
    student[w]="secondDose"
else:
    student[w]="firstDose"
print(student)
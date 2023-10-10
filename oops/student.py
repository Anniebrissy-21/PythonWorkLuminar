class Student:
    reg_num:int
    name:str
    department:str
    gender:str
    age:int

    def __init__(self,reg_num,name,department,gender,age):
        self.reg_num=reg_num
        self.name=name
        self.department=department
        self.gender=gender
        self.age=age

    def display_student(self):
        print(self.reg_num,self.name,self.department,self.gender,self.age)

    def __str__(self):
        return self.name

obj1=Student(1000,"hari","mca","male",23)
#obj1.display_student()

print(obj1)


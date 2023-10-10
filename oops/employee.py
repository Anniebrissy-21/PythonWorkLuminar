class Employee:
    id:int
    name:str
    department:str
    gender:str         #attributes

    def create(self,id,name,dept,gender):
        #initializing attributes
        self.id=id
        self.name=name
        self.department=dept
        self.gender=gender

    def display_emp(self):
        print(self.id,self.name,self.department,self.gender)

emp1=Employee()               #obj1    no of obj can be created by one class
emp1.create(100,"hari","hr","male")
emp1.display_emp()

emp2=Employee()                  #obj2
emp2.create(101,"ravi","it","male")
emp2.display_emp()



        


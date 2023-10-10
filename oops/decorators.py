class Student:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    @property           #decorators
    def get_name(self):
        return self.name
    
    @property
    def get_age(self):
        return self.age
    

obj=Student("hari",23)

#print(obj.get_name)
#print(obj.get_age)


#decorators
def swap_nums(fn):

    def wrapper(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)

        return fn(n1,n2)
    return wrapper

        
@swap_nums
def sub(n1,n2):
    return n1-n2

@swap_nums
def div(n1,n2):
    return n1/n2

print(sub(5,10))
print(div(5,10))



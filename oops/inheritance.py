class Parent:
    phone="Samsung17"
    vehicle="passionpro"

    def mobile(self):
        print(self.phone)

    def bike(self):
        print(self.vehicle)

class Child(Parent):   #will inherit from parent class
    pass          

obj=Child()
obj.mobile()
obj.bike()


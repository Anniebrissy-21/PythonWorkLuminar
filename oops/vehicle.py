class Parent:
    vehicles=["passion pro","swift"]

    def properties(self):
        return self.vehicles
    
class Child(Parent):

    def properties(self):
        self.veh=super().properties()  #super refers the parent class
        self.veh.append("hunter")
        return self.veh
    
ch=Child()
print(ch.properties())
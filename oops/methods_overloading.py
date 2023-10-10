#........methods overloading............
# same method name different no of parameters

class Calculator:
    def add(self,*args):
        return sum(args)
    
obj=Calculator()
print(obj.add(100,200))

    #def add(self,n1,n2):            #method name add    n1...parameter
        #return n1+n2
    
    #def add(self,n1,n2,n3):
        #return n1+n2+n3

    #def add(self,n1,n2,n3,n4):
       # return n1+n2+n3+n4

#obj=Calculator()    

#print(obj.add(12,34))   # this is method overloading ...only last method will take




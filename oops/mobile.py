class Mobile:
    model:str
    brand:str
    network:str
    ram:str
    color:str
    price=int

    def __init__(self,model,brand,network,ram,color,price):    #creat will be changed to constructor __init__
        self.model=model
        self.brand=brand
        self.network=network
        self.ram=ram
        self.color=color
        self.price=price

    #def display_mobile(self):
        #print(self.model,self.brand,self.network,self.ram,self.color,self.price)
    def get(self):
        print(self.model,self.price)

obj1=Mobile("a57","samsung","5g","2gb+36gb","red",24000)   #initializing attrbutes in creating onjects
                  #create=> will initialize instance variables=>constructor
obj1.get()

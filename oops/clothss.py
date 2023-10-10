class cloths:
    data=[
        {"id":1,"name":"lproundneckshirt","brand":"lp","size":"m","color":"red","price":2300},
        
        {"id":2,"name":"lphalfsleeves","brand":"lp","size":"xl","color":"green","price":1000},
            
        {"id":3,"name":"indianterrainshirt","brand":"vh","size":"l","color":"white","price":1400},

        {"id":4,"name":"vanhusenlinen","brand":"vh","size":"m","color":"black","price":2300},
            
    ]

    def get(self,*args,**kwargs):
        return self.data
    
    def retrive(self,*args,**kwargs):
        id=kwargs.get("id")
        rec=[c for c in self.data if c.get("id")==id]
        return rec
    
    def create(self,*args,**kwargs):
        self.data.append(kwargs)

    def destroy(self,*args,**kwargs):
        id=kwargs.get("id")
        rec=[c for c in self.data if c.get("id")==id][0]
        self.data.remove(rec)


obj=cloths()
#print(obj.get())

#print(obj.retrive(id=3))

obj.create(id=5,name="indianterrainshirt",brand="lp",size="l",color="blue",price=3000)
#print(obj.get())

obj.destroy(id=1)
#print(obj.get())


class Mobile:

    data=[
        {"id":1,"model":"Galaxy f53","brand":"Samsung","network":"4g","amound":35000},
        {"id":2,"model":"Realme narzo N55","brand":"Realme","network":"5g","amound":26000},
        {"id":3,"model":"OnePlus Nord CE 3 Lite 5G","brand":"OnePlus","network":"5g","amound":54000},
        {"id":4,"model":"Redmi 10 Power","brand":"Xiaomi","network":"4g","amound":30000},
        {"id":5,"model":"C51","brand":"Poco","network":"5g","amound":45000},
        {"id":6,"model":"F21","brand":"Oppo","network":"4g","amound":19000}
    ]

    #return all  records ->list
    #mobile details->retive
    #add mobile->create
    #edit 
    #delete

    def get(self,*args,**kwargs):
        return self.data
    
    def retrieve(self,*args,**kwargs):
        id=kwargs.get("id")
        records=[m for m in self.data if m.get("id")==id]
        return records
    
    def create(self,*args,**kwargs):
        self.data.append(kwargs)

    def destroy(self,*args,**kwargs):
        id=kwargs.get("id")
        records=[m for m in self.data if m.get("id")==id][0]
        self.data.remove(records)
    
    def update(self,id=None,*args,**kwargs):
        id=id
        rec=[m for m in self.data if m.get("id")==id][0]
        rec.update(kwargs)
        print("mobile is updated")
        
obj=Mobile()
#print(obj.get())

#print(obj.retrieve(id=3))

obj.create(id=7,model="C55",brand="realme",network="4g",amount=23000)
#print(obj.get())

obj.destroy(id=2)
#print(obj.get())

obj.update(id=2,amound=42000)
print(obj.get())



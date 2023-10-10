class Cart:
    cart_details=[
        {"id":1,"item_name":"shirt","price":250,"rating":4.3,"total_quality":1},
        {"id":2,"item_name":"T_shirt","price":400,"rating":4.2,"total_quality":2},
        {"id":3,"item_name":"Earpods","price":1300,"rating":4.7,"total_quality":1},
        {"id":4,"item_name":"tops","price":350,"rating":3.4,"total_quality":3},
        {"id":5,"item_name":"earings","price":130,"rating":4.3,"total_quality":5},

    ]

    #all cart details
    def get(self,*args,**kwargs):
        return self.cart_details

    #add item
    def create(self,*args,**kwargs):
        self.cart_details.append(kwargs)

    #remove items
    def destroy(self,id=None,*args,**kwargs):
        rec=[c for c in self.cart_details if c.get("id")==id][0]
        self.cart_details.remove(rec)

    def add(self,*args,**kwargs):
        total=0
        for c in self.cart_details:
            total+=c.get("price")*c.get("total_quantity")
            return total

obj=Cart()

obj.create(id=6,item_name="short_top",price="234",rating="3.2",total_quantity=2)
#print(obj.get())

obj.destroy(id=1)
print(obj.get())

#print(obj.add())
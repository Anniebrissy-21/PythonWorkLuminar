foods=[
    {"id":1,"name":"ghee-roast","price":70,"category":"veg"},
    {"id":2,"name":"chicken-roast","price":170,"category":"non-veg"},
    {"id":3,"name":"cb","price":120,"category":"non-veg"},
    {"id":4,"name":"bb","price":190,"category":"non-veg"},
    {"id":5,"name":"fried-rice","price":140,"category":"veg"},
    {"id":6,"name":"chicken-friedrice","price":140,"category":"non-veg"},
    {"id":7,"name":"nan","price":70,"category":"veg"},
    {"id":8,"name":"alfham","price":370,"category":"non-veg"},
     
]

# total number of items
# print name whose category = veg
# food names available under rs 100
# costly item
# costly non-veg food

print(len(foods))

veg=[f.get("name") for f in foods if f.get("category")=="veg"]
print(veg)

food_under_rs=[f.get("name") for f in foods if f.get("price")<=100]
print(food_under_rs)

costly=max(foods,key=lambda f:f.get("price"))
print(costly)

non_veg_food=[f for f in foods if f.get("category")=="non-veg"]
costly_nonveg=max(non_veg_food,key=lambda f:f.get("price"))
print(costly_nonveg)

#print all categories
categories={f.get("category") for f in foods }    #{}->duplicates not allowed []->duplicates allowed
print(categories)


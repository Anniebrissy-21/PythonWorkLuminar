items=[
    {"id":1,"name":"sugar","price":40,"avl_qty":10},
    {"id":2,"name":"milk","price":28,"avl_qty":100},
    {"id":3,"name":"teapowder","price":50,"avl_qty":0},
    {"id":4,"name":"tomato","price":120,"avl_qty":80},
    {"id":5,"name":"potato","price":45,"avl_qty":5},
    {"id":6,"name":"carrot","price":78,"avl_qty":0},
    {"id":7,"name":"oreo","price":66,"avl_qty":0},
    {"id":8,"name":"hideandseek","price":20,"avl_qty":60},

]

#no of products
print(len(items))

#available items

for i in items:
    if i.get("avl_qty")>0:
        print(i.get("name"))

#name of product
for i in items:
    print(i.get("name"))

#items >50
for i in items:
    if i.get("price")>50:
        print(i.get("name"))

#product name available in range rs20-rs50

for i in items:
    if i.get("price")>20 and i.get("price")<50:
        print(i.get("name"))

for i in items:
    if i.get("price") in range(20,51):
        print(i.get("name"))


all_product_name=[i.get("name") for i in items]
print(all_product_name)

in_stock_item=[i.get("name") for i in items if i.get("avl_qty")>0]
print(in_stock_item)

price_filter=[i.get("name") for i in items if i.get("price")<=50]
print(price_filter)

range_filter=[i.get("name") for i in items if i.get("price") in range(20,51)]
print(range_filter)

#costly product

price=max([i.get("price") for i in items])
print(price)

costly_product=max(items,key=lambda i:i.get("price"))
print(costly_product)

#sort
product_sort=sorted(items,reverse=True,key=lambda i:i.get("avl_qty"))
print(product_sort)

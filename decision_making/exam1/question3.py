name=input("enter the name:")
person=[{"name":"hari","age":25},
        {"name":"ravi","age":23},
        {"name":"ram","age":21}
]

age=[p.get("age") for p in person if p.get("name")==name][0]
print(age)
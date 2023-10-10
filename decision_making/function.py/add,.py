def add(num1,num2):
    res=num1+num2
    return res

print(add(3,4))


def cube(num):
    res=num**3
    return res

print(cube(4))


def sub(num1,num2):
    res=num1-num2
    return res

print(sub(23,4))



def smart_sub(num1,num2):
    if num1>num2:# return num1-num2 if num1>num2 else retur um2-num1
        return num1-num2
    else:
        return num2-num1
    
print(smart_sub(10,5))




    



def add(*args): #*args for passing more num of parameters
    #print(args)  #* will take as tuple
    return sum(args)
print(add(10,20))

print(add(19,23,45))


def product(*args):
    res=1
    for num in args:
        res*=num

    return res

#print(product(1,2,3,4))

def print_person(*args):
    for v in args:
        print(v)

#print_person("hari",23,"gdh","yrt")



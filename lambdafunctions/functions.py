#lambda fun

#sub
sub=lambda n1,n2:n1-n2
print(sub(20,3))

#cube
cube=lambda n:n**3
print(cube(4))

#largest of two
max_two=lambda n1,n2:n1 if n1>n2 else n2
print(max_two(38,32))

#odd_even
odd_even=lambda n: "even" if n%2==0 else "odd"
print(odd_even(4))

#length of string
get_len=lambda text:len(text)
print(get_len("apple"))

#smart sub
smart_sub=lambda n1,n2:n1-n2 if n1>n2 else n2-n1
print(smart_sub(8,9))




num1=250
num2=20
#temp=num1
#num1=num2
#num2=temp
#values after swapping
# logic 1
# print(f"Values after swapping n1={num1} n2={num2}")

# Logic 2 withod temp
num1=num1+num2
num2=num1-num2
num1=num1-num2
print(f"Values after swapping n1={num1} n2={num2}")
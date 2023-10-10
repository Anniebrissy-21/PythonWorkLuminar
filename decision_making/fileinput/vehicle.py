f=open("D:/pythonwork/decision_making/fileinput/numbers","r")
numbers=[line.rstrip("\n") for line in f]
print(numbers) 


tamilnadu_numbers=[n for n in numbers if n.startswith("tn")]
print(tamilnadu_numbers)



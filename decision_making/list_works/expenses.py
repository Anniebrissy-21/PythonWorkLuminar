expenses=[12000,3000,14000,15000,2000,22000]

total_expenses=sum(expenses)
print(total_expenses)

min_expenses=min(expenses)
print(min_expenses)

max_expenses=max(expenses)
print(max_expenses)

#expenses for feb month

#print(expenses[1])

#for e in expenses:
 #   print(e)


#for e in expenses:
 #   if e>15000:
  #      print(e)

#total=0
#for e in expenses:
 #   total=total+e
#print(total)

#highest expenses
max=0
for e in expenses:
    if e>max:
        max=e
print(max)


#cheapest expense

min=expenses[0]
for e in expenses:
    if e<min:
        min=e
print(min)





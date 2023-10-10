
#         -4    -3     -2       -1
colors=["red","green","blue","yellow","blue"]
#          0     1      2       3
#add->append
colors.append("black")

print(colors)

#remove->pop
colors.pop(1)

print(colors)

#sort
colors.sort()
print(colors)
#reverse sort
colors.sort(reverse=True)
print(colors)

#count
print(colors.count("red"))


#clear
colors.clear()
print(colors)







lst=[2,5,8,32]

# center for loop left return value right condition

#squares
squares=[n**2 for n in lst]
print(squares)

#cubes
cubes=[n**3 for n in lst]
print(cubes)

#add two in every number
add_two=[n+2 for n in lst]
print(add_two)

#num greater than 5
greater=[n for n in lst if n>5]
print(greater)

#even num
even=[n for n in lst if n%2==0]
print(even)

#odd num
odd=[n for n in lst if n%2!=0]
print(odd)

#years between 1800-2026
years=[y for y in range(1800,2026)]
#print(years)

#century years
century_year=[y for y in years if y%100==0]
print(century_year)

#non century years
non_century=[y for y in years if y%100!=0] 
print(non_century)






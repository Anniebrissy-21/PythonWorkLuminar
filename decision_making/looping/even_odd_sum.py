start=10
end=20
odd=0
even=0
#print total sm of all odd_numbers and even_numbers from given start to end

while(start<=end):
    if(start%2==0):
        even=even+start
    else:
        odd=odd+start
        
    start=start+1
print(odd)
print(even)
        


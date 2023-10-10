text=input("enter the text>").casefold()#convert upper case into lowercase
#if(text[0]=="a" or text[0]=="e" or text[0]== "i" or text[0]== "o" or text[0]== "u"):
 #   print("vowels")
#else:
 #   print("consonents")



vowels={"a","e","i","o","u"}
if(text[0] in vowels):
    print("vowels")
else:
    print("consonents")
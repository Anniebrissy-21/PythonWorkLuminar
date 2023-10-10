f=open("D:/pythonwork/decision_making/fileinput/data.txt","r")

#for line in f:
   # print(line)

lst=[]
for line in f:
    lst.append(line.rstrip("\n"))
print(lst)

#longest word
#longest_word=max(lst,key=lambda w:len(w))
#print(longest_word)

words=[line.rstrip("\n") for line in f]
longest_wrd=max(words,key=lambda w:len(w))
#print(longest_wrd)






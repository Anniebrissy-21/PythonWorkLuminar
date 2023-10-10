text="hello good hello goodmorning"

word=text.split(" ")
longest_word=max(word,key=lambda w:len(w))
print(longest_word)




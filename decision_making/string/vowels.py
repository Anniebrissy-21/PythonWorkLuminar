text="Read Latest Live Breaking News and news of india World Sports entertainment Business auto Politics Tech and More"

vowels="a","e","i","o","u"
word=text.split(" ")

for w in word:
    if w.casefold().startswith(vowels):
        print(w)
    
    # if w[0].casefold() in vowels
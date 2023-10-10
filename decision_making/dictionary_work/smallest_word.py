text="hi hello good goodmorning ziyad"

word=text.split(" ")
smallest_word=min(word,key=lambda w:len(w))
print(smallest_word)

#sorted word in reverse order
srt_word=sorted(word,key=lambda w:len(w),reverse=True)
print(srt_word)


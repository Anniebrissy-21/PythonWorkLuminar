f_read=open("D:/pythonwork/tokenization/news.txt")
f_open=open("D:/pythonwork/tokenization/stopwords.txt")

stop_words={line.rstrip("\n") for line in f_open}  #duplicates not needed so set bracets

news_set=set()  #to create empty set

for line in f_read:
    words=line.split()
    for w in words:
        news_set.add(w)  

print(news_set.difference(stop_words))
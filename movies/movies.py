from json import load
path="D:/pythonwork/movies/mdb.json"
with open(path,encoding="utf-8") as f:
    filims=load(f)

#total number of movies
#print(len(filims))

#print all movies name
#filim_names=[f.get("title") for f in filims]
#print(filim_names)

#print 2005 movies

movie=[f.get("title") for f in filims if f.get("year")=="2005"]
#print(movie)

#print movie title whose genre is comedy
com_movies=[f.get("title") for f in filims if "Comedy" in f.get("genres")]
#print(com_movies)

#lengthy movie title
lengthy_movies=max(filims,key=lambda f:int(f.get("runtime")))
#print(lengthy_movies)

#print all genres
genres={g for f in filims for g in f.get("genres")}
#print(genres)

#comedy movies released in 2015
comedy_movies=[f.get("title") for f in filims if "Comedy" in f.get("genres") and f.get("year")=="2015"]
#print(comedy_movies)

wc={}
for f in filims:
    year=f.get("year")
    if year in wc:
        wc[year]+=1
    else:
        wc[year]=1

print(max(wc,key=lambda k:wc.get(k)))



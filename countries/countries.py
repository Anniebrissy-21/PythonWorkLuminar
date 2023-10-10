from json import load
path="D:/pythonwork/countries/countries.json"
with open(path,encoding="utf-8") as f:
    countries=load(f)
print(len(countries))

#for c in countries:
   # print(c.get("name"))

#for c in countries:
    #print(c.get("capital"),c.get("name"))


#longest_population=max(countries,key=lambda c:c.get("population"))
#print(longest_population)

starts_with_c=[c.get("name") for c in countries if c.get("name").casefold().startswith("c")]
#print(starts_with_c)

name_capital=[[c.get("name"),c.get("capital")] for c in countries]
#print(name_capital)

c_with_borders=[c for c in countries if "borders" in c]
max_border_country=max(c_with_borders,key=lambda c:len(c.get("borders")))
#print(max_border_country.get("name"))

#india borders
india_borders=[c.get("borders") for c in countries if c.get("name")=="Afghanistan"][0]
#print(india_borders)
india_border_name=[c.get("name") for c in countries if c.get("alpha3Code") in india_borders]
#print(india_border_name)

region={c.get("region") for c in countries}
print(region)

dependent_countries=[c.get("name") for c in countries if c.get("independent")==False]
#print(dependent_countries)

filter_population=[c.get("name") for c in countries if c.get("population")<400000]
#print(filter_population)

wc={}
for c in countries:
    region_country=c.get("region")
    if region_country in wc:
        wc[region_country]+=1
    else:
        wc[region_country]=1
print(wc)



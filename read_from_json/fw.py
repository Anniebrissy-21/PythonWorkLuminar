from json import load
path="D:/pythonwork/read_from_json/data.json"
#open(path,mode,encoding="utf-8")
with open(path)as f:
    records=load(f)

#print(records)
#for f in records:
    #print(f.get("name"))   
fw_names=[f.get("name") for f in records]   
print(fw_names)

#top rated 
top_rated=max(records,key=lambda d:d.get("rating"))
print(top_rated)

#frontend framework
#python framework




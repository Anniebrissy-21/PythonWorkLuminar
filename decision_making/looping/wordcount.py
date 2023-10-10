text="shycbnxzaqweurcmnzngxyqo ixfn mmaksjurh"
# print vowel count and consonenet count
v_count=0
c_count=0

for ch in text:
    if ch in ["a","e","i","o","u"]:
        v_count+=1
    elif ch!=" ":
        c_count+=1

print("vowel count=",v_count)
print("consonent count=",c_count)

#print "a" not in ch ["a","c"]
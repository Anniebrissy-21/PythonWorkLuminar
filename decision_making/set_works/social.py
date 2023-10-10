all_users=["sachin","dohini","kohli","rohit","sanju","padikkal"]

sanju_followings=["padikkal","sachin"]

suggestions=list(set(all_users).difference(set(sanju_followings)))

sanju_pos=suggestions.index("sanju")
suggestions.pop(sanju_pos)
print(suggestions)


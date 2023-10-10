all_users=["mohanlal","fahad","unny","mamooty","nivin"]
nivin_fiends=["mohanlal","unny","fahad"]
#suggestion for nivin
suggestion_list=[]
for u in all_users:
    if u not in nivin_fiends:
        suggestion_list.append(u)
suggestion_list.pop(suggestion_list.index("nivin"))
print(suggestion_list)

#allusers=["mohanlal","fahad","unny","mamooty","nivin","dq"]
#nivin_friends=["mohanlala","unny","fahad"]
#fahad_friends=["mohanlala","mamooty","unny"]
#list mtual freiends name compared with fahad
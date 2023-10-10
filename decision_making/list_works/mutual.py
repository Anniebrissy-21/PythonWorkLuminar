allusers=["mohanlal","fahad","unny","mamooty","nivin","dq"]
nivin_friends=["mohanlala","unny","fahad"]
fahad_friends=["mohanlala","mamooty","unny"]
#list mtual friends name compared with fahad

for u in allusers:
    if nivin_friends in fahad_friends:
        print(u)
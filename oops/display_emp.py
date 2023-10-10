def display_emp(**kwargs):   #kwags take as dictionary
    #print(kwargs)
    print(kwargs.get("name"))
    print(kwargs.get("salary"))

display_emp(name="hari",dept="hr",n_place="ekm",w_location="tkm",salary=23000)

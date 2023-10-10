def disply_student(**kwargs):
    #print(kwargs)
    print(kwargs.get("name"))
    print(kwargs.get("course"))

disply_student(name="ravi",course="django",rol=1000,gender="male")
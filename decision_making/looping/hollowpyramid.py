for row in range(1,7):
    for col in range(row):
        if row==6|row+col==7|col-row==5:
            print("*")
    print()
while True:

    try:

        x=int(input("enter the number:"))
        y=int(input("enter another number:"))
        z=x/y
        print(z)
        break

    except ValueError:
        print("plz enter a valid number")

    except ZeroDivisionError:
        print("not divide by zero")

    except TypeError:
        print("enter")


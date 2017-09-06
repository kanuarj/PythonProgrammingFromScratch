
while True:

    try:
        a = 10
        nos = int(input("Please enter the number you want\n"))
        b = a / nos
        print(b)
        break

    except Exception:
        print("Something is not right")

    finally:
        print("Code has finished executing")

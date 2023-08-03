def RussianDoll(dollCount):
    if dollCount == 0:
        print("All Dolls are Opened")
    else:
        print(f"Doll to be Opened : {dollCount}")
        RussianDoll(dollCount - 1)


RussianDoll(10)

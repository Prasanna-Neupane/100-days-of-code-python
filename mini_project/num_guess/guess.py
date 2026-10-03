print("welcome to the number guesser!!!!!".title().center(100))
number = 54
tries = 0
while True: 
    num = int(input("enter the guessed number: "))
    if num<10 and num>0:
        print("not close enough to the real number.")

    elif num<20 and num>10:
        print("keep going. you are slowly approaching the target.")

    elif num<30 and num>20:
        print("ummm. just few decades away")

    elif num<40 and num>30:
        print(" slightly off")

    elif num<50 and num>40:
        print("yesss that is a wild guess, but not correct")

    elif num<60 and num>50:
        print("umm you definetly stepping in the tail of lion. Just Few steps away")
        if num<54:
            print("just look around the bush. You already in the area")
        elif num>54:
            print("don't go too far away")
        elif num==54:
            print("and bingo.", end =" ")
            break

    
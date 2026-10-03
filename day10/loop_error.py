
def main():
    # while True:
    #     try: 
    #         roll = int(input("enter your roll number"))
    #     except ValueError:
    #         print("sorry. It was not in the string")
    #     else:
    #         print("your roll number is", roll)
    #         break

    num = input("enter a number: ")
    handle(num)


def handle(x):
    while True:
        try:

            number = int(x)
        except ValueError:
            print("sorry the number you have entered is not an integer.")
            x = input("enter the number again")
        else:
            t = print("the value you entered is integer.")
            return t

main()


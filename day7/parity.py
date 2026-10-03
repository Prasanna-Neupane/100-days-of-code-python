# to check the odd and even number by using modulo and boolean values.
def main():
    num = int(input("enter a number: "))
    if even(num):
        print("the number is even")
    else:
        print("the number is odd")

def even(n):
    print("there are many ways to print the boolean such as true and false")

    #method 1: 
    # if n%2==0:
    #     return True

    # else:
    #     return False


    #method 2: 
    # return True if n%2==0 else False

    print("method 3: ")
    return n%2==0



main()


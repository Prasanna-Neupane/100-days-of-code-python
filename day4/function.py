# def is used for making new function. 
def hello():
    print("hello")


name = "prasanna neupane"
hello()
print(name.title().strip())

#without parameter or argument and return value.
def intro():
    names = input("enter your full name: ")
    age = int(input("how old are you?"))

    print(f"my name is {names.strip().title()} and I am {age} years old", end = ".\n")

print("calling the function to introduce myself. ".capitalize())
intro()
print("\n \n")

#with parameter and no return value
print("#with parameter and no return value")
def write(name):
    print(name)

you = input("Enter your name: ")
write(you)

#we can assign the default value for the empty parameters or the parameters are not assigned with any values

def roundoff(numb = 0):
    x = round(numb)
    print(x)

roundoff()#prints 0 if there is no parameter in the function. 
hii = float(input("enter a number to round off"))
roundoff(hii)


#another way to use function where the function is created after the declaration

def main():
    user1 = int(input("enter a number"))
    user2 = int(input("enter another number"))
    sun = summation(user1, user2)


def summation(x,y):
    z = x+y
    print(z)

main()

#with arguments and return value

def real():
    s = 4
    print("the square of 4 is", square(s))

def square(a):
    return pow(a,2)

real()
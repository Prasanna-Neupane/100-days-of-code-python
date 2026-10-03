#this talks about the error handling
# 1) syntax error. You have to see the syntax error yourself and correct it. No one is going to help you.

x = int(input("enter the value of x in number: "))

print(f"the value of x is {x}")
print("lets assume that the value of x is in letters instead of integers, what do now? It will just show another ValueError. So valueError is used")

try: 
    y = int(input("enter a word but remember that the answer is recieved as the integer: "))
    print("you wrote in the integer")

except ValueError:
    print("you wrote in the letters so this statement showed because and error occured called valueError and i putted some exceptions case saying if ValueError occurs then just print this message.")

print("upto now there are 3 errors.")
print("1. SyntaxError -- error in the grammar of the language.")
print("2. ValueError -- error in the type of value recieved")
print("3. NameError -- when a variable is not defined")

try: #for the NameError
    z = int(input("enter a number: "))
    print(z, "is the number")

except ValueError:
    print("that was not a integer")
else: 
    print(z, "this is good.")


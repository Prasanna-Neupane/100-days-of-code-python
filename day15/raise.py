print("it all about raising the custom error")

num = int(input("enter a number from 0 to 99"))
if num<0 or num>100:
    raise ValueError("do what is asked")

print("lets try to implement the whole error handling")


try:
    number = int(input("enter a number between 5 to 10"))
except ValueError:
    print("Value Error occured yaaaaa")
except Exception as e:
    print("The actual error:", e)
else:
    print("this should not be shown")
finally:
    print("upto now built-in errors are checked")

if number <= 5 or number>=10:
    raise ValueError("please enter the number between 5 and 10")
age = int(input("enter your age"))
if age>18:
    print("you are okay to drive.")
elif age==18:
    print("I doubt you so show me your liscense")
elif age<18:
    print("you are arrested")
else: 
    print("the number you have entered is invalid")

#or 
x = 12
y = 23

if x>y or x<y:
    print("x is not equal to y")
else:
    print("x is equal to y")


if x!=12 or x>y:
    print("x is not equal to 12 and is greater than", y)

elif y!=23 or y>x:
    print("y is not equal to 23 and greater than", x)

if x<y and x>0:
    print(f"{x} is between 0 and {y}")

else:
    print("x is not between them ")


print("lets make some grading system:")

score = int(input("enter your score: "))
if 100 >= score >=95:
    print("You secured A+")
elif 95 > score >=90:
    print("You secured A")
elif 90 > score >=80:
    print("You secured B")
elif 80 > score >=70:
    print("You secured C")
elif 70 > score >=60:
    print("You secured D")
elif 60 > score >=50:
    print("You secured E")
elif 50 > score >=40:
    print("You secured F")
else:
    print("the score entry is invalid.")

print("I performed the above operation using combined statements like: 0<x<1")

print("at first lets talk about the short hand if else statement")

a = 123
b = 12345
print(a,"is greater than",b) if(a>b) else print(b, "is greater than", a) if(a<b) else print("input error")

print("how lets talk about the enumerate function")

marks = [12, 23, 64, 90, 100, 65]
index = 0
for i in marks:
    print("each marks:", i)
    if index == 4:
        print(marks[index], "you got the full marks.")
    index+=1

print("below is the usage of ecumerate function")
for postition, i in enumerate(marks):
    print("each marks:", i)
    if postition == 4:
        print(marks[postition], "you got the full marks.")
    index+=1
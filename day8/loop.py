# While
i = 0
while i<3:
    print(i)
    i = i+1
else:
    print("you are inside the else statement used in the while condition")
print(f" {"---"*30:<30} end")
print(i)

print(f" {"---"*30:<30} end")

for k in range(1,4):
    print(k)
# for loop

# method 1(simplest and the most common method to iterate by for loop)
for a in "hello":
    print(a, end=", ")
print("\n", "---"*30)
# method 2[introduction of lists]

numbers  = [0, 3, 43, 54, 76]
for i in numbers:
    print(i)

# for c in 34:
#     print(c)
# you might expect that the output is 34 or just 3 and 4. but not.
# c tries to look inside the 34 but 34 is the integer there is nothing.

# method 3[you might want to intentionally repeat the loops according to your will]
#intro to the range()

for j in range(5):
    print("my name is prasanna neupane and it is printed 5 times")


#its time for the loop inside the loop

name = ["prasanna", "neupane", "red", "john", "patrick", "jane"]

for nam in name:
    print(nam)
for nam in name:
    print(nam, end=",")

    for i in nam:
        print(i)

#lets do it in more systematic way

for i in name:
    print(i, end="=")
    for j in i:
        print(j, end=",")
    print("\n")



print("just to let you know range(4) = [0, 1, 2, 3]")
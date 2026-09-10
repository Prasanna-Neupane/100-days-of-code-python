#concatination


name= "Prasanna"
surname = "Neupane"
print(name+surname)
print(name, surname)

#how to check the type of variable.
print(type(name))
num = 65432
print("the type of", name, "is", type(name), "and the type of", num, "is", type(num), end=". \n")
#to check the variable of compelex number such as a+ib.
plex = complex(1,2)
#number with pointer
point = 2.222
print("the type of", plex, "is", type(plex), "and the type of", point, "is", type(point))


#updated print format
# print(name, 6, 7, end="% \n", sep="*", file=sys.stdout, flush=False)

#the new way of writting the parameter in the print function

print(f"hello, {name} {surname}. I guess your roll number is {num} and your id is {plex} whereas, your averge gpa is {point}")

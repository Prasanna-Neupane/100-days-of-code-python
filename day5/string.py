#string methods. Just few examples

name = "    prasanna neupane"

print(name.strip())
print(name.lower())
print(name.upper())
print(name.title())
print(name.capitalize())
#combined

trues = name.strip().title()
print(trues)
#indexing the strings
print("individually indexing the characters")
print(trues[0])
print(trues[1])
print(trues[2])
print(trues[3])
print(trues[4])
#to know the length
print(len(trues))
print(len(trues)-3)
print(type(trues))

#same but by the loop
print("looping the each character from the beginning to the end")
for words in trues:
    print(words)



#slicing the characters 

print(trues[:])
print(trues[0:5])
print(trues[:5])

print("negative slicing strings")

print("to identify the different pairs or group will be formed as a group gives same output but by different methods by the members")

print("group 1")
print(trues[0:-3])
print(trues[0:len(trues)-3])
print(trues[0:13])

print("group 2")
print(trues[-1:-4])
print(trues[len(trues)-1:len(trues)-4])
print(trues[15:12])
print("group 2 is empty due to logical error")

print("group 3")
print(trues[-4:-1])
print(trues[len(trues)-4:len(trues)-1])
print(trues[12:15])
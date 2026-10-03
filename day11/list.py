#re studying list.

name = ["prasanna", "sandesh", "jasbin", "abijit"]
roll = [12,45,23,14]
print(len(name))


#to check something in the list we use:

print("to check something in the list we use:")

if 45 in roll:
    print("45 is here")
else:
    print("I am blind")

if "pras" in "prasanna":
    print("true")

#methods of lists
print("methods of lists")

randoms = ["harry", "ball", "catch", "match", "see"]
itch = ["parry", "null", "watch", "patch", "pee"]
num = [1,3,45,23,64,75,8,2552,74,2372,72452,257,24,2572,452,36,246,]

print("randoms = ", randoms)
print("itch = ", itch)

print("ability of apppend is to add one extra word or number")

randoms.append("1added")
print("randoms = ", randoms)

print("count = number of same value present.")
print(num.count(3))

print("sort = ascending order")
num.sort()
print(num)

print("for the descending order use reverse= true inside the sort.")
num.sort(reverse=True)
print(num)

print("for knowing the position, ")
print(itch.index("patch")-1 , "is the position of patch.")

print("some serious simple concept.")
random = randoms
random[1] = "replaced"
print("the value of positioned in 1 is replaced in randoms but the actual changes was made in the random = ", randoms)

print("to stop the connection between the randoms = random, use copy() method.")
ran = randoms.copy()
print(ran, "is the value of ran")

print("if i want to add another list in the current list then use extend(another list variable name)")

randoms.extend(itch)
print(randoms)


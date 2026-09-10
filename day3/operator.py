#operators
#standard 
print(15+6)
print(15%2)
print(15*2)
print(25/2)
print(15-3)

#new
print(25//2)#used to print just the before the point but not after the point. Eg: 2.666-> 2
print(15**3)#exponential. don't use print(15^3) because it has different meaning.

#int

x = input("enter the first number")
y = input("enter the second number")
z = x+y
print(z)


a = input("enter another number")
b = input("enter another number")
c= int(a)+int(b)
print(c)

#float
e = float(input("enter another number"))
f = float(input("enter another number"))

g= e+f
print(g)
# to put commas in respective places.

print(f"with commas: {g:,}")

#roundoff
print(round(g,2))  
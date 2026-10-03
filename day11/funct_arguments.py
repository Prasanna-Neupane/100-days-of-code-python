#revisiting the functions arguments.

def average(a=2,b=2):#the (a=2,b=2) is by default value of a and b. You can remove it by overwriting it.
    avg = (a+b)/2
    print("the average is ",avg)

# average(a=4, b=4)
average(4,4)#priority goes to this value even through there is a default value.

average(8)
#same goes for the string also.
average(b=6,a=9)

print("its about the arbitary argument. ")

#to get the average number as much as you want.

def avgs(*num):
    avgss = (num[0]+num[1])/2

    print("the average is ", avgss)

avgs(6,7)

print("to print the infinite input and get the average.")
def avgss(*num):
    sum =0
    for i in num:
        sum = sum + i
    print("the total sum is", sum)

    print(type(num))
    print(type(i))
    print(type(sum))

avgss(3,46,7)# the value is listed as the tuple.

dictionary = [
    "prasanna", "sandesh", "abijit", "asif", "manish"
]

def dicti(*dictiona):#dictionary is a list but the dictiona recieves as a tuple.
    for i in dictiona:
        
        print(f"the name of student in position {dictionary.index(i)+1} is {i}")

dicti(*dictionary)


name = {
    "prasanna": "evil",
    "sandesh": "hero"
}

def info(**names):
    for i in names:
        print("the name is ", i, "and he is very ", names[i])

info(**name)
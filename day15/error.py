
# try: 
#     num  = int(input("enter a number to be multiplied."))
# except ValueError:
#     print("please enter in the integer.")

# else:
#     for i in range(1,11):
#             print(f"{num}*{i} = {num*i}", end= "\n")
# finally:
#      print("this is always executed. finally must be used when we do some work in the function after return nothing gets printed but if we use finally at the last after the return then it can be printed. ")


# try:
#     a = num
# except Exception as a:
#      print("The real error message: ", a)


# print("there are many error like: indexerror, ZeroDivisionError, ValueError, AttributeError")



print("lets try different types of error.")

print("1) Value error: ")
try: 
    numb = int(input("enter any number: "))
# except Exception as e:
#     print("actual error:", e)
except ValueError:
    print("ValueError was sucessfully checked.")
else: 
    print("Your number is successfully received in the variable.")
finally:
    print("this is printed even though there is error.\n first error trial completed.")

print("2) Type error: ")
try: 
    a = 8
    b = [7]
    sum = a+b
# except Exception as e:
#     print("actual error:", e)
except TypeError:
    print("typeError proved. ")
else:
    print("see this piece of code again. Something is not understandable by you.")
finally:
    print("second error trial completed")

print("3) ZeroDivisionError: ")

try:
    print(2345/0)
# except Exception as e:
#     print("actual error:", e)
except ZeroDivisionError:
    print("ZeroDivisionError proved")
else:
    print("miracle happened. Something is wrong with the computer.")
finally:
    print("third error trial completed.")

try: 
    name = ["prasanna", "Sandesh", "Jasbin"]
    print(name[3])
# except Exception as e:
#     print("actual error:", e)
except IndexError:
    print("IndexError Proved")
else:
    print("error didn't occur but I was expecting error.")
finally:
    print("fourth error trial completed")


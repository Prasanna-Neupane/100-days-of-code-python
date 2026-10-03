print("its about the doc strings and PEP-8")

def main():
    '''This is the function what prints from 0 to 5. doc string is being used to display this sentence'''
    for i in range(6):
        print(i)

main()
print(main.__doc__)
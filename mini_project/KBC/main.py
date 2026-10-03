from category import categories, difficulties
from qa_bank import questions
import questioning

print("welcome to KBC".center(100))
print("Namaste!!!!!!".center(100))

initial = input("dou you want to play KBC \n Ans[y/n]: ")

if initial == "y":
    print("Ko Bancha Krorepati".center(100))
    print("\n")

    print("which category do you want to play?")
    one = 1
    for i in categories:
        print(f"{one}) {i}")
        one+=1

    while True:
        try:
            category_number = int(input("enter the resepective number."))
            category = categories[category_number-1].capitalize()
            print(f"ok you chose {category}")
            break
        except ValueError:
            print("the number you have entered is not correct.")
        except IndexError:
            print("sorry this number is not the correct number. Choose from number 1 to 10")
        
    
    money = 0
    vault = 0
    num_of_question= 1

    
    for i in range(17):

        difficulty = difficulties[num_of_question].capitalize()

        decision = questioning.solution(difficulty, category)

        if decision == "correct":
            print("next question")
            num_of_question+=1

        elif decision == "wrong":
            print("the game is over")
            break
        
            
        

        
    



























elif initial == "n":
    print("I bet you are not smart enough to play KBC")
else:
    print("error!!!!!!. Type according to guidelines.")



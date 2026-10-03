import qa_bank
import random



def solution(difficulty, category):
    main = []
    for i in qa_bank.questions:
        if i["difficulty"]==difficulty and i["category"]==category:
            main.append(i)
            


    original = []
    original = random.choice(main)
    print(f"Q{1}. {[difficulty]}{original["question"]}.")
    
    option_1 = original["choices"][0]
    option_2 = original["choices"][1]
    option_3 = original["choices"][2]
    option_4 = original["choices"][3]

    print(f"1. {option_1}\t\t 2. {option_2} \n 3. {option_3}\t\t 4. {option_4}")

    answer = int(input("Ans[1/2/3/4] = "))

    index_answer = original["answer"]-1 
    
    if answer == original["answer"]:
        print("your answer is correct")
        return("correct")
        
    else:
        print(f"The answer is {original["choices"][index_answer]}.")
        return("wrong")

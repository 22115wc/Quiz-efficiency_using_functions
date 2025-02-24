sec_qs_1 = [2,1,4,"What is the te reo Māori name for NZ?","1. Old Zealand", "2. Aotearoa", "3. Te-ika-a-Maui","4. Australia"]

def quiz(questions):
    for q in questions[3:]:
        print(q)
    user_choice = askQ(questions[1],questions[2])
    if user_choice==questions[0]:
        print("Correct")
    else:
        print("Incorrect")

#reused the below function from my assesment last year
def askQ(minimum,maximum):
    print()
    loopBreak=True
    while loopBreak==True:
        try:
            userInput=int(input("Your choice: "))
            print()
            if userInput<minimum or userInput>maximum:
                print(f"Please enter a number between {minimum} and {maximum}")
                print()
            else:
                loopBreak=False
        except ValueError:
            print()
            print("Please enter only numbers; no letters, spaces or special characters")
            print()
    return userInput

quiz(sec_qs_1)

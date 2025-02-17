sec_qs_1 = [2,1,4,"What is the te reo Māori name for NZ?","1. Old Zealand", "2. Aotearoa", "3. Te-ika-a-Maui","4. Australia"]

def quiz(questions):
    for q in questions[3:]:
        print(q)
    user_choice = askQ(questions[1],questions[2])
    if user_choice==questions[1]:
        print("Correct")
    else:
        print("Incorrect")

#reused the below function from my assesment last year
def askQ(minimum,maximum): #this is probably the most used function. It asks for user input and has all of the error detection you could possibly want. Whenever I ask a question where I need a number response from the user I use this function
    print()
    loopBreak=True
    while loopBreak==True:
        try: #this is a try part of a try-except statement. The program will attempt to execute the program in the try statement
            userInput=int(input("Your choice: "))
            print()
            if userInput<minimum or userInput>maximum:
                print(f"Please enter a number between {minimum} and {maximum}")
                print()
            else:
                loopBreak=False
        except ValueError: #this is an except part of a try-except statement. If a ValueError occurs in the try statement (ie the user doesn't enter a number) this block of code will run. If no ValueError occurs this code is skipped
            print()
            print("Please enter only numbers; no letters, spaces or special characters")
            print()
    return userInput

quiz(sec_qs_1)

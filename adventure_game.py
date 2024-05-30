import time
import random
life = 0
score = 0
def game():
    print("The game started")
    time.sleep(2)
    print("You are in the future")
    time.sleep(2)
    print("All people in the city died!!")
    time.sleep(2)
    print("If you answered all questions you will save he world from zombies")
    time.sleep(2)
    print("You have two ways , go to magition (1),  Enter the castle and kill the king of them (2) ")
    while True:
        input_val = input("Type (1) or (2) : ")
        if input_val == "1":
            magition()
            break
        elif input_val == "2":
            castle()
            break
        else:
            time.sleep(2)
            print("Invalid input. Try again. You must enter 1 or 2")

def magition():

    randomvarcastle = random.choice(["You had made an magic spell and saved the world!!","the zombies had killed you in your way"])
    if randomvarcastle == "You had made an magic spell and saved the world!!":
        score = 90
        life = 90
        time.sleep(2)
        print("Your life is ="+str(life)+" Your score ="+str(score))
        time.sleep(2)
        print(randomvarcastle)

    else:
        score = 10
        life = 0
        time.sleep(2)
        print("Your life is ="+str(life)+" Your score ="+str(score))
        time.sleep(2)
        print(randomvarcastle)       
    play_again()

def castle():
    print("in your way you have met a groub of zombies you have two choises , pick shotgon and fight(1) , escape (2)")
    while True:
        choice = input("Type (1) or (2): ")
        if choice == "1":
            shotgon()
            break
        elif choice == "2":
                score = 10
                life = 0
                time.sleep(2)
                print("Your life is ="+str(life)+" Your score ="+str(score))
                time.sleep(2)
                print("the zombies had chased you")
                time.sleep(2)            
                play_again()
                break
        else:
            time.sleep(2)
            print("Invalid input. Try again. You must enter 1 or 2")

def shotgon():
            randomvar = random.choice(["You have gone to the castle and won the game !!","the zombies had killed you "])
            if randomvar == "You have gone to the castle and won the game !!":
                score = 100
                life = 80
                time.sleep(2)
                print("Your life is ="+str(life)+" Your score ="+str(score))
                time.sleep(2)

                print(randomvar)

            else:

                time.sleep(2)

                score = 20
                life = 0
                print("Your life is ="+str(life)+" Your score ="+str(score))

                print(randomvar)
                time.sleep(2)
                play_again()    



def play_again():
    while True:
        restart = input("Do you want to restart? (yes/no): ")
        if restart == "yes":
            game()
            break
        elif restart == "no":
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Try again. You must enter yes or no")

game()
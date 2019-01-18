## Carel Hernandez
##Rock, Paper, Scissors game

#import Random
import random


##function of the computer choice funtcion
def rsp ():
    computer_choice = random.randint (1,3)
    if computer_choice == 1:
        computer_choice_rock()
    elif computer_choice == 2:
        computer_choice_paper()
    else:
        computer_choice_scissors()

## function when the computer choice is rock
def computer_choice_rock ():
    user_choice = raw_input(" 1 is for Rock, 2 is for Paper, 3 is for scissors: "
if user_choice == "1":
            print " You tied. You chose rock and the computer chose Rock"
                            try_again()
if user_choice == "2":
            print " You won. You chose paper and the computer chose Rock"
                            try_again()
        
if user_choice == "3":
            print " You loss. You chose scissors and the computer chose Rock"
                            try_again()

##function when the computer choice is paper
def computer_choice_paper ():
    user_choice = raw_input(" 1 is for Rock, 2 is for Paper, 3 is for scissors: "
if user_choice == "1":
            print " You loss. You chose rock and the computer chose paper"
                            try_again()
if user_choice == "2":
            print " You tied. You chose paper and the computer chose paper"
                            try_again()
        
if user_choice == "3":
            print " You won. You chose scissors and the computer chose paper"
                            try_again()


##function when the computer choice is scissors
def computer_choice_scissors ():
    user_choice = raw_input(" 1 is for Rock, 2 is for Paper, 3 is for scissors: "
if user_choice == "1":
            print " You won. You chose rock and the computer chose scissors"
                            try_again()
if user_choice == "2":
            print " You loss. You chose paper and the computer chose scissors"
                            try_again()
        
if user_choice == "3":
            print " You tied. You chose scissors and the computer chose scissors"
                            try_again()



##try again function
    def try_again():
        choice= raw_input(" Would you like to challenge the computer again? yes or no?")
                            if choice == "y" or choice == " yes" or choice == "Yes" or choice == "YES":
                            rps ()
                        elif choice == "n" or choice == "No" or choice == "no":
                            quit()
                        else:
                            print " Try Again "
                            try_again()
                          

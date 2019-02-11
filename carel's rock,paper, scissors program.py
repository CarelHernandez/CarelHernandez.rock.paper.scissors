#Carel Hernandez
#Rock, Paper, scissors program


# rock is 1, paper is 2, scissors is 3

#variables
while True: 
    import random
    
#intro 
    print ("lets play rock, paper, scissors!")
    print (" pick rock or paper or scissors")
    player_choice = input ()
#rock
    computer = random.randint (1,3) 
    if player_choice == "rock" and computer == 1:
        print (" you tied with me!")
    if player_choice == "rock" and computer == 2:
        print(" you lost")
    if player_choice == "rock" and computer == 3:
        print (" you won!")

# paper
    if player_choice == "paper" and computer == 1:
        print (" you won!")
    if player_choice == "paper" and computer == 2:
        print (" you tied with me!" )
    if player_choice == "paper" and computer == 3:  
        print (" you lost")
#scissors
    if player_choice == "scissors" and computer == 1:
        print (" you lost")
    if player_choice == "scissors" and computer == 2:
        print(" you won!")
    if player_choice == "scissors" and computer == 3:
        print (" you tied with me")
    

#loop

    question = input (" do you want to try again?")
    if question == "yes" :
        print ("great")

    if question == "no":
        break 















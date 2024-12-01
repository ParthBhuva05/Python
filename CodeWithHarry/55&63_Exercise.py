# 1-- Snack Water Gun

# 2-- snack water and gun is a variation of the childern's game "Rock-Paper-Scissors" where players use hand gestures to represent a snack water and gun. the gun beats the snack and the snack beats the water.

# -- Write apython program to create a snack water and gun game in pythhon using if-else statements.Do not any fancy GUI. Use proper function to check the win.

 
#                          SNACK  WATER  GUN
# computer =               0      1      2       
# players  =   SNACK 0     D      W      L  
#              WATER 1     L      D      W 
#              GUN   2     W      L      D



print("----------WELCOME TO THE GAME----------")
# Import random module
import random
print('Snake - Water - Gun')
 
 
# Input no. of rounds
n = int(input('Enter number of rounds: '))
 
 
# List containing Snake(s), Water(w), Gun(g)
options = ['s', 'w', 'g']
 
# Round numbers
rounds = 1
 
# Count of computer wins
comp_win = 0
 
# Count of player wins
user_win = 0
 
 
# There will be n rounds of game
while rounds <= n:
 
    # Display round
    print(f"Round :{rounds}\nSnake - 's'\nWater - 'w'\nGun - 'g'")
 
    # Exception handling
    try:
        player = input("Choose your option: ")
    except EOFError as e:
        print(e)
 
    # Control of bad inputs
    if player != 's' and player != 'w' and player != 'g':
        print("Invalid input, try again\n")
        continue
 
    # random.choice() will randomly choose
    # item from list- options
    computer = random.choice(options)
 
    # Conditions based on the game rule
    if computer == 's':
        if player == 'w':
            comp_win += 1
        elif player == 'g':
            user_win += 1
 
    elif computer == 'w':
        if player == 'g':
            comp_win += 1
        elif player == 's':
            user_win += 1
 
    elif computer == 'g':
        if player == 's':
            comp_win += 1
        elif player == 'w':
            user_win += 1
 
    # Announce winner of every round
    if user_win > comp_win:
        print(f"You Won round {rounds}\n")
    elif comp_win > user_win:
        print(f"Computer Won round {rounds}\n")
    else:
        print("Draw!!\n")
 
    rounds += 1
 
 
# Final winner based on the number of wons
if user_win > comp_win:
    print("Congratulations!! You Won")
elif comp_win > user_win:
    print("You lose!!")
else:
    print("Match Draw!!")





# # ----------  Harry code   ----------

# import random

# def check(comp, user):
#     if comp == user:
#         return 0 
    
#     if (comp == 0) and (user == 1):
#         return -1
    
#     if (comp == 1) and (user == 2):
#         return -1

#     if (comp == 2) and (user == 0):
#         return -1

#     return 1


# comp = random.randint(0,2)
# user = int(input("0 for Snack, 1 for Water and 2 for Gun: "))


# score = check(comp, user)

# print("Your Chose Option is: ", user)
# print("Computer Chose Option is: ", comp)

# if (score == 0):
#     print("It is Draw")

# elif (score == 1):
#     print("You Win The Game")

# else:
#     print("You Lose the Game")




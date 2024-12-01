# Exercise_3: Kaun Banega Crorepati(KBC)

# Create a program capable of displaying questions to the user like KBC.

# Use list data type to store the questiion and their correct answer.

# Display the final amount the person is taking home after playing the game.

questions = [
["Which language was used to create facebook ?"
 "Python", "Php", "Javascript", "None", 4],

["Which language was used to create facebook ?"
 "Python", "Php", "Javascript", "None", 4],

["Which language was used to create facebook ?"
 "Python", "Php", "Javascript", "None", 4],

["Which language was used to create facebook ?"
 "Python", "Php", "Javascript", "None", 4],

["Which language was used to create facebook ?"
 "Python", "Php", "Javascript", "None", 4],

 ["Which language was used to create facebook ?"
 "Python", "Php", "Javascript", "None", 4],

["Which language was used to create facebook ?"
 "Python", "Php", "Javascript", "None", 4],

["Which language was used to create facebook ?"
 "Python", "Php", "Javascript", "None", 4],

["Which language was used to create facebook ?"
 "Python", "Php", "Javascript", "None", 4],

["Which language was used to create facebook ?"
 "Python", "Php", "Javascript", "None", 4],

 ["Which language was used to create facebook ?"
 "Python", "Php", "Javascript", "None", 4],

["Which language was used to create facebook ?"
 "Python", "Php", "Javascript", "None", 4],

["Which language was used to create facebook ?"
 "Python", "Php", "Javascript", "None", 4],

["Which language was used to create facebook ?"
 "Python", "Php", "Javascript", "None", 4],

["Which language was used to create facebook ?"
 "Python", "Php", "Javascript", "None", 4],

 ["Which language was used to create facebook ?"
 "Python", "Php", "Javascript", "None", 4],

["Which language was used to create facebook ?"
 "Python", "Php", "Javascript", "None", 4],

["Which language was used to create facebook ?"
 "Python", "Php", "Javascript", "None", 4],

["Which language was used to create facebook ?"
 "Python", "Php", "Javascript", "None", 4],

["Which language was used to create facebook ?"
 "Python", "Php", "Javascript", "None", 4],
]


levels = [1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000, 2000000, 5000000, 10000000, 20000000, 50000000, 70000000]
money = 0
i = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\nquestion for Rs. {levels[i]}")
    print(f"a. {question[1]}             b. {question[2]}")
    print(f"c. {question[3]}             d. {question[4]}")
    reply = int(input("Enter your answer (1-4) or 0 to quit "))
    if (reply == 0):
        money = levels[i-1]
        break
    if (reply == question[-1]):
        print(f"Correct answer, you have Won Rs. {levels[i]}")
        if(i ==4):
            money = 20000
        elif (i == 9):
            money = 1000000
        elif (i == 14):
            money = 50000000
    else:
        print("Wrong answer !")
        break

print(f"Your take home money is {money}")
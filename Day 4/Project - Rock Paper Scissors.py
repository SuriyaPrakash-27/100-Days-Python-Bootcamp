import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player_input == 0:
    print(rock)
elif player_input == 1:
    print(paper)
elif player_input == 2:
    print(scissors)
else:
    print('Invalid Input')

comp_input = random.randint(0,2)

if comp_input == 0:
    print(rock)
elif comp_input == 1:
    print(paper)
else:
    print(scissors)

if player_input == 0:
    if comp_input == 0:
        print("Its a draw")
    elif comp_input == 1:
        print("You Lose")
    elif comp_input == 2:
        print("You Win")

if player_input == 1:
    if comp_input == 0:
        print("You Win")
    elif comp_input == 1:
        print("Its a draw")
    elif comp_input == 2:
        print("You Lose")

if player_input == 2:
    if comp_input == 0:
        print("You Lose")
    elif comp_input == 1:
        print("You Win")
    elif comp_input == 2:
        print("Its a draw")







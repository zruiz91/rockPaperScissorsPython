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

#Write your code below this line 👇
import random

choices = [rock, paper, scissors]

user_choice = choices[int(input("What do you choose? Typer 0 for Rock, 1 for Paper or 2 for Scissors.\n"))]

print(user_choice)

cpu_choice = choices[random.randint(0, 2)]

print("Computer chose: \n" + cpu_choice)

if (cpu_choice == rock and user_choice == scissors):
  print("you lose")
elif (cpu_choice == scissors and user_choice == rock):
  print("you win")
elif (cpu_choice == scissors and user_choice == paper):
  print("you lose")
elif (cpu_choice == paper and user_choice == scissors):
  print("you win")
elif (cpu_choice == paper and user_choice == rock):
  print("you lose")
elif (cpu_choice == rock and user_choice == paper):
  print("you win")
elif (cpu_choice == user_choice):
  print("Draw")
else:
  print("answer not readable")
# Who's paying
import random

seed = int(input("Enter the seed number:"))

random.seed(seed)

namesasCSV = input("Enter everybody's names, separated by a comma.\n")
names = namesasCSV.split(", ")

length = len(names)

a = random.randint(0, length-1)

print(f"{names[a]} is going to pay for the meal today!")


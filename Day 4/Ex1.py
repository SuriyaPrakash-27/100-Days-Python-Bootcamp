# Heads or Tails generator
import random

seed = int(input("Enter your seed number:"))

random.seed(seed)

a = random.randint(0,1)

if a==0:
    print("Heads")
else:
    print("Tails")
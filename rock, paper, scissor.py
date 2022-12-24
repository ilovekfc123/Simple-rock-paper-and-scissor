import random

while True:
    user = input("Rock, paper and scissor: ")   
    num = random.randint(1,3)
    if num == 1: print("rock")
    if num == 2: print("paper")
    if num == 3: print("scissor")

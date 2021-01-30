import random

while True:
    guess = int(input())
    if guess == 0:
        break       
    num1 = random.randint(1,100)
    print(num1)



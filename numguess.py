import random

while True:
    guess = int(input())
    if guess ==0:
        print('OK BYEBYE SEE YOU LATER.')
        break       
    num1 = random.randint(1,100)
    print(f'ANSWER : {num1}')
    print(f'YOUR ANSWER : {guess}')



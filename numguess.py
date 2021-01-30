"""
이 게임은 numguess게임으로 사용자가 컴퓨터가 낸 랜덤한 값을 맞추는 게임입니다
"""
import random

while True:
    guess = int(input())
    if guess == 0:
        break       
    num1 = random.randint(1,100)
    print(num1)



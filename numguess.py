"""
이 게임은 numguess게임으로 사용자가 컴퓨터가 낸 랜덤한 값을 맞추는 게임입니다
"""
import random
cnt = 5
while cnt != 0:
    num1 = random.randint(1,100)
    guess = int(input())

    if guess != num1:
        print('NOPE !')
        cnt -=1
print('GAME OVER')  

import random


def play():
    rand = random.randint(1, 6)
    if rand == 1:
        print(f'------------\n|          |\n|    0     |\n|          |\n------------')
    if rand == 2:
        print(f'------------\n|          |\n| 0      0 |\n|          |\n------------')
    if rand == 3:
        print(f'------------\n|    0     |\n|    0     |\n|    0     |\n------------')
    if rand == 4:
        print(f'------------\n| 0      0 |\n|          |\n| 0      0 |\n------------')
    if rand == 5:
        print(f'------------\n| 0      0 |\n|    0     |\n| 0      0 |\n------------')
    if rand == 6:
        print(f'------------\n| 0      0 |\n| 0      0 |\n| 0      0 |\n------------')


play()

answer = input('Press y to roll again ')
while answer == 'y':
    play()
    answer = input('Press y to roll again ')

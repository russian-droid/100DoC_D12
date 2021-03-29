import random
the_number = random.randint(0,100)

start='''
____________________________________________

-------------NUMBER GUESSING GAME-----------

I'm thinking of a number between 1 and 100.
You need to guess it.
____________________________________________
'''
print(start)
print(f'*{the_number}\n\n')

level=input("Choose a difficulty level. Type 'easy' or 'hard'\n")
if level == 'easy':
    print('Level EASY: you\'ve got 10 attempts to guees it.\n')
elif level == 'hard':
    print('Level HARD: you\'ve got 5 attempts to guees it.\n')
else:
    print('Incorrect entry')

running_game = True

guess=int(input("Make a guess: "))
if guess == the_number:
    print(f'***You won!***\nCorrect, the number was {the_number}')
    running_game = False
else:
    if guess > the_number:
        print('  Too high. Try again.')
    elif guess < the_number:
        print('  Too low. Try again')

#You have 5 attempts remaining to guess the number.

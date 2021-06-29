import random
print('Guess what the outcome of the coin toss will be! Make sure your guess is either \'heads\' or \'tails\'.')
guess = input().lower()
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Once again, you can only enter \'heads\' or \'tails\':')
    guess = input().lower()

toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == 1:
    toss = str('heads')
elif toss == 0:
    toss = str('tails')

if toss == guess.lower():
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess.lower():
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
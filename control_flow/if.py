
number = 23

guess = int(input('Enter an integer : '))

if guess == number:
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
elif guess < number:
    print('No, number is a little higher than guess')
else:
    print('No, number is little lower than guess')
print('Done')


number = 23
running = True

while running:
    guess = int(input('Enter an integer : '))

    if guess == number:
        print('Congratulations, you guessed it.')
        running = False
    elif guess < number:
        print('No, number is little higher than guess.')
    else:
        print('No, number is little lower than guess.')
else:
    print('The while loop is over.')
print('Done')

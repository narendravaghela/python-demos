# Simple Code Guessing Game
import random

def generate_code():
    '''
    Generates a ramdom 3 digits code
    '''
    digits = [str(number) for number in range(10)]
    random.shuffle(digits)
    return digits[:3]

def get_user_guess():
    '''
    Get the input from user
    Convert it into list for further processing
    '''
    return list(input('Your guess: '))

def guess_result(guess, generated_code):
    '''
    Check the user guess against the generated code
    and return the result with possible matches
    '''
    result = []

    # if user entered same code
    if guess == generated_code:
        return 'Bingo'

    # Check for possible matches
    for index, number in enumerate(guess):
        if number == generated_code[index]:
            result.append('Match')
        elif number in generated_code:
            result.append('Close')

    # If no matches
    if result == []:
        return ['Nope']
    else:
        return result

# Main game logic
print('Welcome to code guessing game!')

# Generate a new code
computer_code = generate_code()
print(computer_code)

# Get user input until the correct guess
result = []
while result != 'Bingo':
    user_input = get_user_guess()

    # check result
    result = guess_result(user_input, computer_code)

    # display the result
    if result == 'Bingo':
        print('Hey, it is correct number!')
    else:
        for res in result:
            print(res)

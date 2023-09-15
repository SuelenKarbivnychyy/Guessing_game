import random

def guessing_game():
    """A number-guessing game."""

    user_name = input("Howdy, what's your name? ")
    print(f"\n{user_name}, I'm thinking of a number between 1 and 100.\nTry to guess my number.\n" )    
    attempt = 1
    computer_number = random.randint(1, 100)
    # print(computer_number)
    game_is_on = True

    while game_is_on:

        try:
            user_guess = int(input("Your guess? "))               
        except ValueError:
            print("\nYou bastard provided something that is not a number. Please provide a number next time.")     
        else:
            if user_guess < 1 or user_guess > 100:
                print("\nHey bastard you enter a number that is not in the range a asked you! Try better next time.")     
            elif user_guess < computer_number:
                attempt += 1
                print("Your guess is too low, try again.\n")        
            elif user_guess > computer_number: 
                attempt += 1
                print("Your guess is too high, try again.\n")
            else:    
                game_is_on = False        
                return f"Well done, {user_name}! You found my number in {attempt} tries!"     


print(guessing_game())
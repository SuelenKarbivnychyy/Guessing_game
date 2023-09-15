import random

def guessing_game():
    """A number-guessing game."""

    user_name = input("Howdy, what's your name? ")
      
    attempt = 1
    best_score = 0
    use_max_attempt = 10    
    pc_attempt = 1
    
    user_wants_to_choose_range = input(f"\nHello {user_name} would you like to choose a range for you to guess? (y/n) or if you wants the computer to play enter (PC): ").upper()
    if user_wants_to_choose_range == "N":
        print(f"\n{user_name}, I'm thinking of a number between 1 and 100.\nTry to guess my number.\n" )  
        computer_number = random.randint(1, 100)
    elif user_wants_to_choose_range == "PC":

        computer_guess = random.randint(1, 100)
        high = 0
        low = 0

        while True:      
            print(f"PC guess: {computer_guess}")
            user_hint = input("Give me feedback: ").upper()
            if user_hint == "TOO HIGH": 
                high = computer_guess                              
                computer_guess = random.randint(low, computer_guess - 1)                                                
                pc_attempt += 1
                
            elif user_hint == "TOO LOW":     
                low = computer_guess            
                computer_guess = random.randint(computer_guess + 1, high)                                              
                pc_attempt += 1
            else:
                return f"Uhullllll I got it in {pc_attempt} tries"   
                
    else:
        user_range_starts = int(input("\nFrom which number should the range starts? (You can choose any number from 1 to 100): "))
        user_range_end = int(input("\nIn which number should the range ends? (Choose a number up to 100): "))
        computer_number = random.randint(user_range_starts, user_range_end)
        print(f"\nI'm thinking of a number between {user_range_starts} and {user_range_end}.\nTry to guess my number.\n")


    game_is_on = True

    while game_is_on:        

        try:
            user_guess = int(input("Your guess? "))               
        except ValueError:
            print("\nYou bastard provided something that is not a number. Please provide a number next time.")     
        else:
            if attempt > use_max_attempt:
                print("You are out of chances.")
                play_again = input("\nWould you like to play again? (Y/n): ").upper()
                if play_again == "Y":
                    computer_number = random.randint(1, 100)                    
                    attempt = 1
                    continue
                else:
                    game_is_on = False
                    return "\nThank you for playing."

            elif user_guess < 1 or user_guess > 100:
                print("\nHey bastard you enter a number that is not in the range I asked you! Try better next time.")     
            elif user_guess < computer_number:
                attempt += 1
                print("Your guess is too low, try again.\n")        
            elif user_guess > computer_number: 
                attempt += 1
                print("Your guess is too high, try again.\n")
            else:                        
                print (f"\nWell done, {user_name}! You found my number in {attempt} tries!")

                if best_score == 0:
                    best_score = attempt
                elif attempt < best_score:
                    best_score = attempt

                    print("You got the best score ever, You are now the line lider for this game with only {best_score} tries. Congrats")    

                play_again = input("\nWould you like to play again? (Y/n): ").upper()   
                if play_again == "Y":
                    computer_number = random.randint(1, 100)                    
                    attempt = 1
                    continue                
                else:
                    game_is_on = False
                    return "\nThank you for playing."

print(guessing_game())
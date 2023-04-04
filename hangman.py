"""
Loop max turn count 6
Get a guess
Check guess
If wrong increase count
Print correct letters
If all correct, break
"""

# The secret word the player is trying to guess
secret_word = "CBTNuggets"
letters_guessed = ""

# The number of turns before the player loses
failure_count = 6

# Loop until the player has made too many failed attempts
# will break loop if they succeed instead
while failure_count > 0:
    
    # Get the guessed letter from the players
    guess = input("Enter a letter: ")
    
    if guess in secret_word:
        print(f"Correct there is one or more {guess} in the secret word.")
    else:
        failure_count -= 1
        print(f"Incorrect, there is no {guess} in the secret word. {failure_count} turn(s) left.")
        
    # Maintain a list of all letters guessed
    letters_guessed = letters_guessed + guess
    wrong_letter_count = 0
    
    for letter in secret_word:
        if letter in letters_guessed:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            wrong_letter_count += 1
        
    # If there were no wrong letters, then the player won!
    if wrong_letter_count == 0:
        print(f"Congrats! The secret word was: {secret_word}. You won!")
        break
        
else:
    print("Sorry you didn't win it this time. Try again!")
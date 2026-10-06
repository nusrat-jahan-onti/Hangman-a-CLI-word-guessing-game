# Hangman Game
# ------------
# A simple console game. The computer picks a secret word and you
# guess it one letter at a time, or you can try to guess the whole word.
# You choose a level (easy, medium or hard) which decides how many
# wrong guesses you are allowed.
#
# How to run:  python hangman.py

import random   # we need this to pick a random word

# ---------- Game data ----------

# The secret words
words = ["python", "apple", "school", "planet", "window"]

# A hint for each word. The hint at position 0 belongs to the word at
# position 0, the hint at position 1 belongs to the word at position 1, etc.
hints = [
    "A popular programming language",
    "A fruit",
    "A place where students learn",
    "Earth is one of these",
    "You look through it",
]

# Drawings of the hangman. stages[0] is the empty gallows (no mistakes)
# and stages[6] is the full hangman (game over).
# The r before the quotes lets us print the \ symbol without any problem.
stages = [
    r"""
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========""",
]

wins = 0        # how many games the player has won
losses = 0      # how many games the player has lost

print("=== HANGMAN GAME ===")

# ---------- Main loop: keeps playing while the player says "y" ----------

play_again = "y"

while play_again == "y":

    # Step 1: let the player choose a level
    level = ""
    while level != "1" and level != "2" and level != "3":
        print("\nChoose a level:")
        print("1 - Easy   (8 wrong guesses allowed, with hint)")
        print("2 - Medium (6 wrong guesses allowed, with hint)")
        print("3 - Hard   (4 wrong guesses allowed, no hint)")
        level = input("Enter 1, 2 or 3: ")

    if level == "1":
        max_wrong = 8
        show_hint = True
    elif level == "2":
        max_wrong = 6
        show_hint = True
    else:
        max_wrong = 4
        show_hint = False

    # Step 2: pick a random word (and its hint) for this game
    number = random.randint(0, len(words) - 1)
    secret_word = words[number]
    hint = hints[number]

    # Step 3: set up the starting values for this game
    guessed_letters = []   # all the letters the player has tried
    wrong_guesses = 0      # how many mistakes so far
    won = False            # becomes True when the word is found

    print("\nNew game! The word has", len(secret_word), "letters.")
    if show_hint:
        print("Hint:", hint)

    # Step 4: keep asking for guesses until the player wins or loses
    while wrong_guesses < max_wrong and won == False:

        # Show the hangman drawing. There are always 7 drawings (0 to 6),
        # so we turn the mistakes into a number from 0 to 6.
        # Example: on hard (4 chances), 2 mistakes show drawing number 3.
        stage_number = wrong_guesses * 6 // max_wrong
        print(stages[stage_number])

        # Build the word to show: correct letters are shown, others are _
        display = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display = display + letter + " "
            else:
                display = display + "_ "

        print("\nWord:", display)
        print("Wrong guesses left:", max_wrong - wrong_guesses)
        print("Letters guessed:", guessed_letters)

        # Ask for a letter, or for the whole word
        guess = input("Enter a letter (or the whole word): ").lower()

        # Check the guess
        if not guess.isalpha():
            print("Please use letters only.")
        elif len(guess) > 1:
            # The player is trying to guess the whole word
            if guess == secret_word:
                won = True
            else:
                print("Wrong word!")
                wrong_guesses = wrong_guesses + 1
        elif guess in guessed_letters:
            print("You already tried that letter.")
        else:
            # It is a new letter, so remember it
            guessed_letters.append(guess)

            if guess in secret_word:
                print("Good guess!")
            else:
                print("Wrong guess!")
                wrong_guesses = wrong_guesses + 1

            # Check if the player has found all the letters
            won = True
            for letter in secret_word:
                if letter not in guessed_letters:
                    won = False

    # Step 5: the game is over, show the result
    if won:
        print("\nYou won! The word was:", secret_word)
        wins = wins + 1
    else:
        print(stages[6])
        print("\nYou lost! The word was:", secret_word)
        losses = losses + 1

    print("Score -> Wins:", wins, " Losses:", losses)

    # Step 6: ask if the player wants another game
    play_again = input("\nPlay again? (y/n): ").lower()

print("Thanks for playing!")

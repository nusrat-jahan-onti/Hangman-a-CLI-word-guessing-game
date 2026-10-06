# Hangman Game

A simple Hangman game for the console, written in Python.
The computer picks a secret word and you guess it one letter at a time,
or you can try to guess the whole word. Choose a level, then find the word
before you run out of wrong guesses.

## Features

- Three levels: easy, medium and hard
- Picks a random word from a list of 5 words
- Shows a hint for the word (easy and medium)
- Guess one letter at a time, or type the whole word
- Draws the hangman step by step as you make mistakes
- Tells you if you type something that is not a letter, or repeat a letter
- Keeps your score (wins and losses)
- Lets you play again and choose a new level

## Levels

| Level | Wrong guesses allowed | Hint |
|---|---|---|
| 1 - Easy | 8 | Yes |
| 2 - Medium | 6 | Yes |
| 3 - Hard | 4 | No |

## What You Need

- Python 3 installed on your computer
- Nothing else. No extra libraries.

## How to Run

### On your computer

```bash
python hangman.py
```

(On some computers you need to type `python3 hangman.py`.)

### In Google Colab

1. Go to [colab.research.google.com](https://colab.research.google.com) and make a new notebook.
2. Copy everything from `hangman.py` into a code cell.
3. Click the Run button.
4. Type your answers in the box that appears under the cell.

## How to Play

1. Choose a level by typing 1, 2 or 3.
2. The game shows how many letters the word has (and a hint on easy and medium).
3. Each missing letter is shown as `_`.
4. Type **one letter** and press Enter. If it is in the word, it appears in the right place.
5. Or type the **whole word**. If you are right, you win straight away. If you are wrong, you lose one chance.
6. Every wrong guess makes the hangman drawing grow.
7. Find the word before you run out of chances to win.
8. At the end, type `y` to play again or `n` to stop.

## Example

```text
=== HANGMAN GAME ===

Choose a level:
1 - Easy   (8 wrong guesses allowed, with hint)
2 - Medium (6 wrong guesses allowed, with hint)
3 - Hard   (4 wrong guesses allowed, no hint)
Enter 1, 2 or 3: 2

New game! The word has 5 letters.
Hint: A fruit

     +---+
     |   |
         |
         |
         |
         |
    =========

Word: _ _ _ _ _
Wrong guesses left: 6
Letters guessed: []
Enter a letter (or the whole word): p
Good guess!
...
Enter a letter (or the whole word): apple

You won! The word was: apple
Score -> Wins: 1  Losses: 0

Play again? (y/n):
```

## Project Files

```text
hangman-game/
├── hangman.py          the game
├── docs/
│   └── HOW_IT_WORKS.md explanation of the code
├── README.md           this file
└── .gitignore          files Git should not upload
```

## Change the Game

- **Different words:** change the `words` list in `hangman.py`. Change the `hints` list too, and keep the same order.
- **Different number of chances:** change the numbers `8`, `6` and `4` in the level choice part of the code (and the text of the menu).

## Idea to Add Later

- Word categories such as animals or fruits

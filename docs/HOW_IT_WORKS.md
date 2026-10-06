# How the Hangman Game Works

This file explains the code in `hangman.py` step by step.

## 1. The data at the top

| Name | What it is | What it does |
|---|---|---|
| `words` | list | The 5 secret words |
| `hints` | list | One hint for each word, in the same order |
| `stages` | list | 7 drawings of the hangman (0 mistakes to full hangman) |
| `wins`, `losses` | numbers | The score |

The numbers `max_wrong` (how many wrong guesses are allowed) and `show_hint`
are set later, when the player chooses a level.

## 2. Steps of the program

The game is made of loops, one inside another.

**Outer loop** (runs while the player wants to play again)

1. **Choose a level.** A small `while` loop keeps asking until the player types 1, 2 or 3. Then `if / elif / else` sets the values:

   | Level | `max_wrong` | `show_hint` |
   |---|---|---|
   | 1 - Easy | 8 | `True` |
   | 2 - Medium | 6 | `True` |
   | 3 - Hard | 4 | `False` |

2. **Pick a word.** `random.randint(0, len(words) - 1)` gives a random position in the list. The same position is used for the word and its hint.
3. **Set up the game.** `guessed_letters` starts as an empty list, `wrong_guesses` starts at 0 and `won` is `False`. The hint is printed only if `show_hint` is `True`.
4. **Play** (the inner loop, see below).
5. **Show the result.** The player wins or loses and the score is updated.
6. **Ask to play again.** If the answer is not `y`, the loop stops.

**Inner loop** (runs while the player has chances left and has not won)

1. Print the drawing (see section 3).
2. Build the word to show. A `for` loop goes through each letter of the secret word. If the letter is in `guessed_letters` it is added to the text, otherwise `_` is added.
3. Ask for a guess with `input()`. `.lower()` changes capital letters to small ones.
4. Check the guess with `if / elif / else`:
   - Not made of letters only: show a message.
   - More than one letter: the player is guessing the **whole word**. If it is equal to the secret word, `won` becomes `True`. If not, add 1 to `wrong_guesses`.
   - A letter that was already tried: show a message.
   - A new letter: add it to `guessed_letters`, then check if it is in the word. If it is not, add 1 to `wrong_guesses`.
5. After a new letter, check for a win. Start with `won = True`, then go through the word. If any letter is not yet guessed, set `won = False`.

## 3. How the drawing works with different levels

There are always 7 drawings (number 0 to 6), but each level allows a different
number of mistakes. This line changes the mistakes into a drawing number:

```python
stage_number = wrong_guesses * 6 // max_wrong
```

The `//` sign divides and drops the decimals. Examples:

| Level | Mistakes | Calculation | Drawing number |
|---|---|---|---|
| Easy (8) | 4 | 4 * 6 // 8 | 3 |
| Medium (6) | 3 | 3 * 6 // 6 | 3 |
| Hard (4) | 2 | 2 * 6 // 4 | 3 |

When the player uses all the chances, the full drawing (number 6) is shown.

## 4. Example with the word "apple" (medium level)

| Player types | What happens | Word shown |
|---|---|---|
| `p` | Correct letter | `_ p p _ _` |
| `z` | Wrong letter, 1 mistake | `_ p p _ _` |
| `banana` | Wrong word, 2 mistakes | `_ p p _ _` |
| `apple` | Right word, the player wins | `a p p l e` |

## 5. Python ideas used

| Idea | Where in the code |
|---|---|
| `random` | Choosing the secret word |
| `while` loop | Playing the game, choosing a level and playing again |
| `for` loop | Showing the word and checking for a win |
| `if / elif / else` | Setting the level and checking each guess |
| Strings | `.lower()`, `.isalpha()`, `len()`, adding text together |
| Lists | `words`, `hints`, `stages`, `guessed_letters` |
| `input()` and `print()` | Talking to the player |

## 6. Things to try

- Add a 6th word and hint.
- Change the number of chances for a level.
- Show a message like "Last chance!" when only 1 wrong guess is left.

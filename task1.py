import random

# Predefined list of words
words = ["apple", "mango", "grape", "tiger", "house"]

# Choose a random word
word = random.choice(words)

# Create blanks for each letter
display = ["_"] * len(word)

# Store guessed letters
guessed_letters = []

# Maximum wrong guesses
chances = 6

print("WELCOME TO HANGMAN")

# Loop until player wins or loses
while chances > 0 and "_" in display:

    print("\nWord:", " ".join(display))
    print("Wrong chances left:", chances)

    # Player guesses ONE LETTER
    guess = input("Guess a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed this letter!")

    else:
        guessed_letters.append(guess)

        # If guessed letter is correct
        if guess in word:
            print("Correct!")

            # Reveal the letter in the word
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess

        # If guessed letter is wrong
        else:
            print("Wrong!")
            chances -= 1

# Final result
if "_" not in display:
    print("\nYou Won!")
    print("The word was:", word)

else:
    print("\nYou Lost!")
    print("The word was:", word)

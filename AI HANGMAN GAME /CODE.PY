import random

# List of words to choose from
word_list = ["python", "hangman", "programming", "computer", "gaming", "artificial"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(word_list)

# Function to display the current state of the word
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# Function to play the Hangman game
def play_hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            print("Incorrect guess. You have", attempts - 1, "attempts left.")
            attempts -= 1

        current_state = display_word(word, guessed_letters)
        print(current_state)

        if "_" not in current_state:
            print("Congratulations, you've won! The word was:", word)
            break

    if attempts == 0:
        print("Sorry, you've run out of attempts. The word was:", word)

if __name__ == "__main__":
    play_hangman()

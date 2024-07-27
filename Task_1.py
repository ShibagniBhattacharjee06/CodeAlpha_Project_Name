import random

def choose_word():
    words = ["physics", "chemistry", "biology", "mathematics", "python"]
    return random.choice(words)

def display_current_progress(word, guesses):
    return " ".join([letter if letter in guesses else "_" for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    
    print("\nWELCOME TO THE HANGMAN GAME")
    print(display_current_progress(word, guessed_letters))
    
    while incorrect_guesses < max_incorrect_guesses:
        guess = input("\nGuess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabetical letter.")
            continue
        
        if guess in guessed_letters:
            print("You have already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print(f"Correct guess! The current word is: {display_current_progress(word, guessed_letters)}")
        else:
            guessed_letters.add(guess)
            incorrect_guesses += 1
            print(f"Wrong guess. You have {max_incorrect_guesses - incorrect_guesses} incorrect guesses left.")
            print(display_current_progress(word, guessed_letters))
        
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        print(f"\nSorry, you've run out of guesses. The word was: {word}")

def main():
    while True:
        hangman()
        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing Hangman! Goodbye!")
            break

if __name__ == "__main__":
    main()

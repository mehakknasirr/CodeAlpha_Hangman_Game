
import random

# Predefined list of 5 words as per task requirements
word_list = ["python", "codealpha", "developer", "program", "internship"]
secret_word = random.choice(word_list)

# Track game state
guessed_word = ["_"] * len(secret_word)
max_attempts = 6
guessed_letters = []

print("Welcome to Hangman!")

# Main game loop
while max_attempts > 0 and "_" in guessed_word:
	print("\nWord to guess: " + " ".join(guessed_word))
	print(f"Attempts remaining: {max_attempts}")
	print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
    
	guess = input("Guess a letter: ").lower().strip()
    
	# Input validation
	if len(guess) != 1 or not guess.isalpha():
		print("Please enter a single valid letter.")
		continue
        
	if guess in guessed_letters:
		print("You already guessed that letter! Try another one.")
		continue
        
	guessed_letters.append(guess)
    
	# Check if character matches
	if guess in secret_word:
		print(f"Good job! '{guess}' is in the word.")
		for index, letter in enumerate(secret_word):
			if letter == guess:
				guessed_word[index] = guess
	else:
		print(f"Oops! '{guess}' is not in the word.")
		max_attempts -= 1

# End of game check
if "_" not in guessed_word:
	print(f"\n🎉 Congratulations! You guessed the word: {secret_word}")
else:
	print(f"\n💀 Game Over! You ran out of attempts. The word was: {secret_word}")

# Day 7 of 100 - Hangman

import random
import hangman_art
import hangman_words 

chosen_word = random.choice(hangman_words.word_list)

print(f'Pssst, the solution is {chosen_word}.')

word_length = len(chosen_word)
end_of_game = False
lives = 6

print(hangman_art.logo)

display = []
for _ in range(word_length):
    display += "_"
print(display)

while not end_of_game:
    
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter      
        
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("You lost!")
            end_of_game = True

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(hangman_art.stages[lives])


print("You win!")

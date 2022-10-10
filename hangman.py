import random , hangman_art , hangman_words


life = len(hangman_art.stages)
print(hangman_art.logo)
word_list = hangman_words.word_list
pc_word = random.choice(word_list)
#print(pc_word)
user_word = ['_' for letter in pc_word]
print(' '.join(user_word))

while ''.join(user_word) != pc_word and life > 0:
    guess = input("Enter a letter : ").strip().lower()

    if guess not in pc_word:
        life -= 1
        
    for pos in range(len(pc_word)):
        if pc_word[pos] == guess:
            user_word[pos] = guess
    print(' '.join(user_word))
    print(hangman_art.stages[life])

if life == 0:
    print(f"life ended . You loose. the word was {pc_word}")
else:
    print(f"You guessed the word")

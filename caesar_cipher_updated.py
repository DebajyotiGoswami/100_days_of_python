import caesar_cipher_art
data = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

print(caesar_cipher_art.logo)

def caesars(user_word , shift_amount , direction):
    new_word = ''
    if direction == 'decode':
        shift_amount *= -1
    for letter in user_word:
        if letter in data:
            word_pos = data.find(letter)
            new_word += data[word_pos + shift_amount]
        else:
            new_word += letter
    return new_word

while True:
    coding_choice = input("What do you want ? 'encode' or 'decode' ? ").strip().lower()
    if coding_choice not in ('encode' , 'decode'):
        print("wrong choice")
    else:
        user_word = input("Enter the word : ").strip().lower()
        shift_amount = int(input("Enter the shift amount : ")) % 26
        new_word = caesars(user_word , shift_amount , coding_choice)
        print(f"The {coding_choice}d string is {new_word}")

data = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

def encode(user_word , shift_amount):
    encoded_word = ''
    for letter in user_word:
        word_pos = data.find(letter)
        encoded_word += data[word_pos + shift_amount]
    print(f"Encoded word is {encoded_word}")

def decode(user_word , shift_amount):
    decoded_word = ''
    for letter in user_word:
        word_pos = data.find(letter)
        decoded_word += data[word_pos - shift_amount]
    print(f"Decoded word is {decoded_word}")
    
while True:
    coding_choice = input("What do you want ? 'encode' or 'decode' ? ").strip().lower()
    if coding_choice not in ('encode' , 'decode'):
        print("wrong choice")
    else:
        user_word = input("Enter the word : ").strip().lower()
        shift_amount = int(input("Enter the shift amount : "))
        if coding_choice == 'encode':
            encode(user_word , shift_amount)
        else:
            decode(user_word , shift_amount)

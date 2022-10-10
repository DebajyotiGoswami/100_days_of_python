## this program was not in the course . It suddently came in my head
## 10.10.2022 : interchange between capital and small letters

def modify_string(text):
    small = "abcdefghijklmnopqrstuvwxyz"
    capital = small.upper()

    modified_text = ""

    for letter in text:
        if letter in small:
            modified_text += capital[small.index(letter)]
        elif letter in capital:
            modified_text += small[capital.index(letter)]
        else:
            modified_text += letter

    return modified_text

text = input("Enter your text to change : ")
print(f"Modified string is {modify_string(text)}")

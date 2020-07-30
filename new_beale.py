import string
from decipher import decode

def choose_cipher():

    print("The Beale Cipher")
    user_input = input("Please enter which text you would like to test. 1 for Cipher 1, 2 for Solved Cipher 2, and 3 for Cipher 3: ")
    print()

    if user_input not in ["1", "2", "3"]:
        print("Please input a 1, 2 or 3.")
        return

    with open('text.txt', 'r') as file1:
        text_data = file1.read()

    punc = string.punctuation

    for j in range(len(punc)):
        text_data = text_data.replace(punc[j], "")

    with open('numbers{}.txt'.format(int(user_input)), 'r') as file2:
        number_data = file2.read()

    print(decode(number_data, text_data))

choose_cipher()

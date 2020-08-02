import string

def choose_cipher():

    print("The Beale Cipher")
    user_input = input("Please enter which number cipher you would like to test: ")
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

def decode(number_data, text_data):
    words = str(text_data).split()
    numbers = str(number_data).split(",")
    string = ""
    max = 0

    for k in range(len(numbers)):
        cur_num = int(numbers[k])
        if cur_num > max:
            max = cur_num

    if len(words) > max:
        for i in range(len(numbers)):
            word_index = int(numbers[i])
            word_at_index = words[word_index]
            first_letter = word_at_index[0]
            string = string + first_letter
    else:
        string = "Number of words in this text are not enough for it to qualify as the key"

    return string

choose_cipher()

import string

with open('text.txt', 'r') as file1:
    text_data = file1.read()

punc = string.punctuation

for j in range(len(punc)):
    text_data = text_data.replace(punc[j], "")

words = str(text_data).split()

with open('numbers1.txt', 'r') as file2:
    number_data = file2.read().replace(',', ' ')

numbers = str(number_data).split()

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

print(string)

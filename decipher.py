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

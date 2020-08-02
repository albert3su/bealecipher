import tkinter as tk
import string

class Application(tk.Frame):
    # constructor for the Application
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    # makes all the widgets by calling their respective functions
    def create_widgets(self):
        self.create_quit()
        self.create_cipher_choices()
        self.create_decrypt()

    def create_decrypt(self):
        def clicked():
            print(self.decode_cipher(self.selected.get()))

        btn = tk.Button(self, text="Decrypt!", bg="white", fg="green", command=
            clicked)
        btn.pack(side="left")

    # creates the quit button
    def create_quit(self):
        quit = tk.Button(self, text="Quit", bg="white", fg="red", command=self.master.destroy)
        quit.pack(side="right")

    # creates radio buttons with the cipher choice
    def create_cipher_choices(self):
        # assigns three radio buttons, one for each cipher text
        self.selected = tk.IntVar()
        rad1 = tk.Radiobutton(self, text="Cipher 1", value=1, variable=self.selected)
        rad2 = tk.Radiobutton(self, text="Cipher 2", value=2, variable=self.selected)
        rad3 = tk.Radiobutton(self, text="Cipher 3", value=3, variable=self.selected)

        # packs the buttons
        rad1.pack(side="left")
        rad2.pack(side="left")
        rad3.pack(side="left")

    # reads data from chosen cipher text
    def decode_cipher(self, num_cipher):
        with open('key.txt', 'r') as file1:
            text_data = file1.read()

        punc = string.punctuation

        for j in range(len(punc)):
            text_data = text_data.replace(punc[j], "")

        with open('cipher{}.txt'.format(int(num_cipher), 'r')) as file2:
            number_data = file2.read()

        words = str(text_data).split()
        numbers = str(number_data).split(",")
        result = ""
        max = 0

        for k in range(len(numbers)):
            cur_num = int(numbers[k])
            if cur_num > max:
                max = cur_num

        if len(words) > max:
            for i in range(len(numbers)):
                word_index = int(numbers[i])
                word_at_index = words[word_index]
                print(word_at_index)
                first_letter = word_at_index[0]
                result = result + first_letter
        else:
            result = "Number of words in this text are not enough for it to qualify as the key"

        return result

root = tk.Tk()
root.title('Beale Cipher Decoder')
root.geometry('960x540')

app = Application(master=root)
app.mainloop()

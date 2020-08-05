import tkinter as tk
import string
from tkinter.ttk import *




class Application(tk.Frame):
    # constructor for the Application
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    # makes all the widgets by calling their respective functions
    def create_widgets(self):
        self.create_output("")
        self.create_tail()
        self.create_cipher_choices()
        self.create_quit()
        self.create_decrypt()

    # creates tail label
    def create_tail(self):
        lbl = tk.Label(self, text="Please select a cipher and key, then press decrypt to test your key!\nYour decrypted message will be displayed above!")
        lbl.pack()

    # creates display box for text
    def create_output(self, txt):
        self.display = tk.Text(self)
        self.display.insert("end", txt)
        self.display.pack()
        self.display.config(state="disabled")

    # creates the decrypt button
    def create_decrypt(self):
        decrypt_style = Style()
        decrypt_style.configure('decrypt.TButton', font=('georgia', 10), foreground='green')

        def clicked():
            self.display.config(state='normal')
            self.display.delete('1.0', "end")
            self.display.insert("end", "\n" + self.decode_cipher(self.selected.get()))
            self.display.config(state="disabled")

        btn = Button(self, text="Decrypt!", style='decrypt.TButton', command=
            clicked)
        btn.pack(side="left")

    # creates the quit button
    def create_quit(self):
        quit_style = Style()
        quit_style.configure('quit.TButton', font=('georgia', 10), foreground='red')

        quit = Button(self, text="Quit", style='quit.TButton', command=self.master.destroy)
        quit.pack(side="right")

    # creates radio buttons with the cipher choice
    def create_cipher_choices(self):
        # assigns three radio buttons, one for each cipher text
        self.selected = tk.IntVar()
        rad1 = tk.Radiobutton(self, text="Cipher 1", value=1, variable=self.selected)
        rad2 = tk.Radiobutton(self, text="Cipher 2", value=2, variable=self.selected)
        rad3 = tk.Radiobutton(self, text="Cipher 3", value=3, variable=self.selected)

        # packs the buttons
        rad1.pack()
        rad2.pack()
        rad3.pack()

    # decodes cipher
    def decode_cipher(self, num_cipher):
        #reads data in the key file
        with open('key.txt', 'r') as file1:
            text_data = file1.read()

        # removes punctuation from text
        punc = string.punctuation
        for j in range(len(punc)):
            text_data = text_data.replace(punc[j], "")

        # if no cipher is chosen then prompt user
        if num_cipher not in [1,2,3]:
            return "Please choose a cipher!"

        # read cipher text specified if cipher is chosen
        with open('cipher{}.txt'.format(int(num_cipher), 'r')) as file2:
            number_data = file2.read()

        # split data from read files
        words = str(text_data).split()
        numbers = str(number_data).split(",")

        # define return string and max variable
        result = ""
        max = 0

        # find highest number in the cipher text
        for k in range(len(numbers)):
            cur_num = int(numbers[k])
            if cur_num > max:
                max = cur_num

        # checks if the number of words in key is greater than the highest number
        # if not, return a message indicating so
        if len(words) > max:
            for i in range(len(numbers)):
                word_index = int(numbers[i])
                result += words[word_index][0]
        else:
            return "The number of words in this text are not enough for it to qualify as the key."

        # returns the decrypted message along with a display msg
        return "Here's your decrypted message!\n\n" + result.upper()

root = tk.Tk()
root.title('Beale Cipher Decoder')
root.geometry('960x540')

app = Application(master=root)
app.mainloop()

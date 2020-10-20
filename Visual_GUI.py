import tkinter as tk
import numpy as np
import tkinter.font as tkFont
from PIL import ImageTk,Image
import random
import pandas as pd


class values:
    test_type = 0
    score = 0
    i = 1
    no_questions = 0
    error = ""
    language = ""
    random_word_a = ""
    random_word_b = ""
    translations = ""
    dictionary = ""
    ans = ""
    count = 0
    p = 0

class Demo1:
    def __init__(self, master):
        self.window = master

        # Fullscreen code
        self.window.attributes('-fullscreen', True)
        self.fullScreenState = False
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)
        self.img = ImageTk.PhotoImage(Image.open("Tree.jpg"))
        self.label = tk.Label(self.window, image=self.img)
        self.label.pack(anchor="n", fill="both", expand=True, side="left" )
        self.start_page()
    def start_page(self):

    #Background Image

        self.button_font = tkFont.Font(family="Times", size=20)
        self.exit_font = tkFont.Font(family="Times", size=15)
        # Exit Button Code
        self.button_exit = tk.Button(self.window, text='Exit', width=25, height=1, bd=2, command=self.window.destroy, font=self.exit_font)
        self.button_exit.place(relx=0.9, rely=0.9, anchor="center")

        # Start Test Button Code

        self.button_test = tk.Button(self.window, text='Start Test', width=25, bd=2, command=self.testing, font=self.button_font)
        self.button_test.place(relx=0.5, rely=0.4, anchor="center")

        # Adding Words Button Code
        self.button_words = tk.Button(self.window, text='Adding New Words', width=25, bd=2, command=self.word_add, font=self.button_font)
        self.button_words.place(relx=0.5, rely=0.5, anchor="center")



        # self.frame = tk.Frame(self.master)
        # self.frame.pack()

        self.window.mainloop()

    def testing(self):
        values.i = 1
        values.score = 0
        self.button_words.destroy()
        self.button_test.destroy()


        self.pick_type = tk.Label(self.window, text="Pick test type: ", font=self.button_font)
        self.pick_type.place(relx=0.5, rely=0.3, anchor="center")
        self.E_G = tk.Button(self.window, text="English to German", font=self.button_font, command=self.eng_ger)
        self.E_G.place(relx=0.4, rely=0.5, anchor="center")
        self.G_E = tk.Button(self.window, text="German to English", font=self.button_font, command=self.ger_eng)
        self.G_E.place(relx=0.6, rely=0.5, anchor="center")

    def eng_ger(self):
        values.test_type = 2
        self.making_no_q()

    def ger_eng(self):
        values.test_type = 1
        self.making_no_q()

    def making_no_q(self):
        self.E_G.destroy()
        self.G_E.destroy()
        self.pick_type.destroy()
        self.num = tk.Label(self.window, text="How many questions would you like in the test: ", font=self.button_font)
        self.num.place(relx=0.5, rely=0.3, anchor="center")
        self.next1 = tk.Button(self.window, text="Next", font=self.button_font, command=self.error_check)
        self.next1.place(relx=0.5, rely=0.7, anchor="center")
        self.entry1 = tk.Entry(self.window, width=10, bd=10, font=self.button_font)
        self.entry1.place(relx=0.5, rely=0.5, anchor="center")
        self.entry1.focus()
        self.window.bind("<Return>", self.enter_press1)

    def enter_press1(self, event):
        try:
            self.error_check()
        except:
            return


    def error_check(self):

        try:
            no_questions1 = int(self.entry1.get())
            values.no_questions = no_questions1
        except ValueError:
            values.error = "Invalid Character - Please enter an integer for the number of questions"
            self.new_window_error()
            return

        if no_questions1 < 1:
            values.error = "Input less than 0 - Pick an integer greater than 0"
            self.new_window_error()
            return
        else:
            self.translations_fnc()

    def translations_fnc(self):
        self.dict()

        if values.i == 1:
            self.num.destroy()
            self.entry1.destroy()
            self.next1.destroy()
        if values.i != 1:
            self.result_label.destroy()
            self.next2.destroy()
        h = random.randrange(0, len(values.translations))
        if values.test_type == 1:
            values.random_word_a = values.dictionary[h][1]
            values.random_word_b = values.dictionary[h][0]
            values.language = "English"
        else:
            values.random_word_a = values.dictionary[h][0]
            values.random_word_b = values.dictionary[h][1]
            values.language = "German"
        self.ask_translation = tk.Label(self.window, text="What is the "+values.language+" for \""+values.random_word_a+"\"?: ", font=self.button_font)
        self.ask_translation.place(relx=0.5, rely=0.3, anchor="center")
        self.submit = tk.Button(self.window, text="Next", font=self.button_font, command=self.answer_check)
        self.submit.place(relx=0.5, rely=0.7, anchor="center")
        self.entry2 = tk.Entry(self.window, width=10, bd=10, font=self.button_font)
        self.entry2.place(relx=0.5, rely=0.5, anchor="center")
        self.entry2.focus()
        self.window.bind("<Return>", self.enter_press2)

    def enter_press2(self, event):
        try:
            self.answer_check()
        except:
            return

    def answer_check(self):
        ans = self.entry2.get()
        values.ans = ans
        values.i = values.i + 1
        self.ask_translation.destroy()
        self.submit.destroy()
        self.entry2.destroy()

        if ans == values.random_word_b or ans == values.random_word_b.lower() or ans.lower() == values.random_word_b or ans.lower() == values.random_word_b.lower():
            values.score = values.score + 1
            self.result_label = tk.Label(self.window, text="That is the correct answer", font=self.button_font)
            self.result_label.place(relx=0.5, rely=0.3, anchor="center")
            if values.i <= values.no_questions:
                end_test = "Next Question"
            else:
                end_test = "Results"
            self.next2 = tk.Button(self.window, text=end_test, font=self.button_font, command=self.test_end)
            self.next2.place(relx=0.5, rely=0.7, anchor="center")
        else:
            self.result_label = tk.Label(self.window, text="That is incorrect, the correct answer was " + values.random_word_b, font=self.button_font)
            self.result_label.place(relx=0.5, rely=0.3, anchor="center")
            if values.i <= values.no_questions:
                end_test = "Next Question"
            else:
                end_test = "Results"
            self.next2 = tk.Button(self.window, text=end_test, font=self.button_font, command=self.test_end)
            self.next2.place(relx=0.5, rely=0.7, anchor="center")
        self.window.bind("<Return>", self.enter_press3)

    def enter_press3(self, event):
        try:
            self.test_end()
        except:
            return

    def test_end(self):
        if values.i <= values.no_questions:
            self.translations_fnc()
        else:
            self.results_screen()
            self.window.unbind("<Return>")


    def results_screen(self):
        self.result_label.destroy()
        self.next2.destroy()
        self.overall_score = tk.Label(self.window, text="Your score was  "+str(values.score)+" out of "+str(values.no_questions), font=self.button_font)
        self.overall_score.place(relx=0.5, rely=0.3, anchor="center")
        self.another = tk.Label(self.window, text="Would you like to do another test?: ", font=self.button_font)
        self.another.place(relx=0.5, rely=0.4, anchor="center")
        self.yes_test = tk.Button(self.window, text="Yes", font=self.button_font, command=self.again)
        self.yes_test.place(relx=0.4, rely=0.7, anchor="center")
        self.no_test = tk.Button(self.window, text="No", font=self.button_font, command=self.home_screen)
        self.no_test.place(relx=0.6, rely=0.7, anchor="center")

    def again(self):
        self.overall_score.destroy()
        self.another.destroy()
        self.yes_test.destroy()
        self.no_test.destroy()
        self.testing()

    def home_screen(self):
        self.overall_score.destroy()
        self.another.destroy()
        self.yes_test.destroy()
        self.no_test.destroy()
        self.start_page()

    def dict(self):
        file = open("GermanDictionary.txt", "r")
        translations = file.read().split("-")
        values.translations = translations
        for i in range(0, len(translations)):
            translations[i] = translations[i].split(';')
        path = np.array(translations)
        Dictionary = [[s.rstrip("\n") for s in nested] for nested in path]
        values.dictionary = Dictionary
        return






    def word_add(self):
        self.button_words.destroy()
        self.button_test.destroy()
        self.add_eng = tk.Label(self.window, text="Write the english here: ", font=self.button_font)
        self.add_eng.place(relx=0.5, rely=0.3, anchor="center")
        self.add_ger = tk.Label(self.window, text="Write the German translation here: ", font=self.button_font)
        self.add_ger.place(relx=0.5, rely=0.5, anchor="center")
        self.write_eng = tk.Entry(self.window, width=10, bd=10, font=self.button_font)
        self.write_eng.place(relx=0.5, rely=0.4, anchor="center")
        self.write_eng.focus()
        self.write_ger = tk.Entry(self.window, width=10, bd=10, font=self.button_font)
        self.write_ger.place(relx=0.5, rely=0.6, anchor="center")
        self.Home = tk.Button(self.window, text="Home Screen", font=self.exit_font, width=25, height=1, bd=2, command=self.home_from_add)
        self.Home.place(relx=0.1, rely=0.9, anchor="center")
        self.add = tk.Button(self.window, text="Add word to dictionary", font=self.button_font, command=self.add_words)
        self.add.place(relx=0.5, rely=0.7, anchor="center")

    def add_words(self):
        with open("GermanDictionary.txt", "r+") as f1:
            eng = self.write_eng.get()
            ger = self.write_ger.get()
            if ger != "" and eng != "":
                f1.write("-" + eng + ";" + ger + "\n")
            pd.Index(f1).duplicated(keep="first")
            self.write_eng.delete(0, "end")
            self.write_ger.delete(0, "end")
            values.count = values.count + 1
            self.word_count()
            return

    def word_count(self):

        if values.p != 0:
            self.counter.destroy()
            values.p = values.p + 1
        if values.count == 1:
            counted = "You have added 1 word to the dictionary so far"
        else:
            counted = "You have added " + str(values.count) + " words to the dictionary so far"
        self.counter = tk.Label(self.window, text=counted, font=self.button_font)
        self.counter.place(relx=0.5, rely=0.8, anchor="center")


    def home_from_add(self):
        self.Home.destroy()
        self.add.destroy()
        self.add_ger.destroy()
        self.add_eng.destroy()
        self.write_eng.destroy()
        self.write_ger.destroy()
        self.counter.destroy()
        self.start_page()




        # Fullscreen code
    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)


    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)


    #Pop-up Window
    def new_window_error(self):
        self.newWindow = tk.Toplevel(self.window)
        self.newWindow.geometry("100x50+900+300")
        self.app = error_win(self.newWindow)

class error_win:
    def __init__(self, master):
        self.master = master

        self.error_label = tk.Label(self.master, text=values.error)
        self.error_label.pack()
        self.quitButton = tk.Button(self.master, text="Close", command = self.close_windows)
        self.quitButton.pack()
        self.master.geometry("400x50+750+400")
    def close_windows(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    Demo1(root)


if __name__ == '__main__':
    main()

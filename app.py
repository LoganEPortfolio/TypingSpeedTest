from tkinter import *
import random
import time
from english_words import get_english_words_set

web2lowerset = list(get_english_words_set(['web2'], lower=True))
# print(web2lowerset)
# print(type(web2lowerset))

root = Tk()
root.title('Typing Speed Test')
root.config(padx=50, pady=20)
#root.geometry('400x320')


user_input_var = StringVar()
user_input_list = []
#@phrase_list = ['word', 'test', 'phone', 'another']


def build_random_list():
    phrase_list = []
    for _ in range(10):
        phrase_list.append(random.choice(web2lowerset))
    return phrase_list
    
phrase_list = build_random_list()
print(phrase_list)

def space_event(event=None):
    user_input = user_input_var.get()
    user_input_list.append(user_input.strip())
    user_entry.delete(0, 'end')
    print(user_input_list)

    

def run_test(time_delta):
    correct_list = [i for i,j in zip(phrase_list, user_input_list) if i == j]
    print(len(correct_list))
    wpm = (len(correct_list)) // (time_delta/60)
    print(wpm)
    return wpm
    


def start(event):
    global start_time
    start_time  = time.time()
    print(start_time)

def stop(event):
    stoptime = time.time()
    print(stoptime)
    time_delta = stoptime - start_time
    print(stoptime - start_time)
    wpm = round(run_test(time_delta), 2)
    wpm_text.config(text=f"WPM: {wpm}")

instructions = Label(text="Press Left CTRL to start.  Press Enter to end.")
instructions.config(wraplength=350, font=('Arial', 20))
instructions.grid(column=0, row=0, pady=(0, 50))

phrase = Label(text=phrase_list)
phrase.config(wraplength=200, font=('Arial', 15))
phrase.grid(column=0, row=2)

user_entry = Entry(textvariable=user_input_var)
user_entry.grid(column=0, row=3, pady=(5, 20))


wpm_text =Label(text="WPM: 0")
wpm_text.grid(column=0, row=4)

root.bind("<Control_L>", start)
root.bind("<space>", space_event)
root.bind("<Return>", stop)
root.mainloop()


from tkinter import *
import random


root = Tk()

root.title('Typing Speed Test')
user_input_var = StringVar()

def random_phrase_fn():
    return random.randint(0,5)

def run_script():
    user_input = user_input_var.get()
    print(user_input)
    random_phrase = random_phrase_fn()
    phrase.config(text=random_phrase)

random_phrase = random_phrase_fn()
print(random_phrase)

phrase = Label(text=random_phrase)
phrase.grid(column=0, row=0)

user_entry = Entry(textvariable=user_input_var)
user_entry.grid(column=0, row=1)


submit = Button(text='Submit', command=run_script)
submit.grid(column=1, row=2)

root.mainloop()


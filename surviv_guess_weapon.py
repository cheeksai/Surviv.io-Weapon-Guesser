import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
import random
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import PhotoImage
import tkinter as tk

pd.options.mode.chained_assignment = None

df = pd.read_csv('/home/jacks/tests/surviv_weapons_data.csv')
columns = df.columns
weapons = df[columns[0]]
fire_types = df[columns[1]]
for idx, i in enumerate(df[columns[2]]):
    i = f'/home/jacks/tests/icons/{idx}.png'
    df[columns[2]][idx] = i
icons = df[columns[2]]
weapon_types = df[columns[3]]
ammo = df[columns[4]]
magazine_totals = df[columns[5]]
damage = df[columns[6]]
fire_rates = df[columns[7]]
dps = df[columns[8]]
reload = df[columns[9]]
features = df[columns[10]]
date_added = df[columns[11]]
how_to_counter = df[columns[12]]

index = random.randint(0,92)
weapon = df.iloc[index]
answer = weapon[0]






window = Tk()
window.title('Weapon Selection:')

yscrollbar = Scrollbar(window)
yscrollbar.pack(side = RIGHT, fill = Y)

label = Label(window,
              text = "Guess the weapon",
              font = ("Times New Roman", 10), 
              padx = 10, pady = 10)
label.pack()
list = Listbox(window, selectmode = "browse", 
               yscrollcommand = yscrollbar.set)

list.pack(padx = 10, pady = 10,
          expand = YES, fill = "both")

x = weapons

for each_item in range(len(x)):
    
    list.insert(END, x[each_item])
    list.itemconfig(each_item, bg = "lime")

yscrollbar.config(command = list.yview)

attempts = {"value": 0}

hints = []
hints.append(f'Hint: {features[index]}')
hints.append(f'Hint: {fire_rates[index]} fire rate')
hints.append(f'Hint: {reload[index]} reload time')
hints.append(f'Hint: {damage[index]} damage')
hints.append(f'Counter: {how_to_counter[index]}')
hints.append(f'Hint: {magazine_totals[index]} bullets in 1 magazine')
hints.append(f'Hint: {ammo[index]} ammo')
hints.append('Icon')
random.shuffle(hints)

index_for_icon = random.randint(0,len(hints))

rand_num = len(hints) - 1
if hints[rand_num] != 'Icon':
    label = Label(window,
        text = hints[rand_num],
        font = ("Times New Roman", 10), 
        padx = 10, pady = 10)
else:
    image = PhotoImage(file=icons[index]).subsample(5,5)
    label = Label(window, image=image)
    label.image = image
label.pack()
hints.pop(rand_num)

def handle_item_select(event, attempts_ref):
    rand_num = len(hints) - 2
    guess = list.curselection()
    guess = ",".join([list.get(i) for i in guess])
    if attempts_ref['value'] < 7 and guess != answer:
        if hints[rand_num] != 'Icon':
            label = Label(window,
                text = hints[rand_num],
                font = ("Times New Roman", 10), 
                padx = 10, pady = 10)
        else:
            image = PhotoImage(file=icons[index]).subsample(5,5)
            label = Label(window, image=image)
            label.image = image
        label.pack()
        hints.pop(rand_num)
        rand_num -= 1

    if guess != answer:
        attempts_ref['value'] += 1
        result = showinfo(
        title='Your Guess:', 
        message=f'{guess} is incorrect'
    )
    else:
        attempts_ref['value'] += 1
        result = showinfo(
        title='Your Guess:', 
        message=f'{answer} is correct\n{attempts_ref['value']} tries'
    )
        if result == "ok":
            window.destroy()
            
list.bind('<<ListboxSelect>>', lambda e: handle_item_select(e, attempts))

window.mainloop()
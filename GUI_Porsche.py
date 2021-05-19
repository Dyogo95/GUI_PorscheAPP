#!/usr/bin/env Python3
from tkinter import *
import tkinter as tk
from get_TMs import get_TM_names_list
from tkcalendar import Calendar
import pandas as pd
from datetime import datetime
import locale

# Tkinter Window setup
window = tk.Tk()
window.geometry("800x800")
Title = tk.Label(text="Standard Customer responses", font='Helvetica 18 bold')

# Seperators
sep_TM_date = tk.Label(text="____________________________________\nWhen did the customer sent the email?")
sep_date_gender = tk.Label(text="____________________________________\nWhat's the customers gender?")
sep_gender_CustomerName = tk.Label(text="____________________________________\nWhat's the customers name?\n")
sep_CustomerName_Subject = tk.Label(text="____________________________________\nIhre Anfrage... vom")
sep_subj = tk.Label(text="z.B.: 'zur Bewerbung'", font='Helvetica 11 italic')
sep_subj_case = tk.Label(text="____________________________________\nWhat's the case number?\n")
sep_case_agent = tk.Label(text="____________________________________\nWhat's your name?\n")

locale.setlocale(locale.LC_ALL, 'de_DE')

def return_from_dropdown(dropdown):
    return dropdown.get()


# 1. TM Drop down Box
# def select_TM():
with open('Porsche_TM_vereinfacht.txt') as f:
    # Read the file fully and as string. Name it TM
    TM = f.read()
    # Split TM by "----------" to seperate each module
    modules = TM.split("----------")

TM = StringVar(window)
TM_titles = get_TM_names_list.get_TM_names(modules)
TM.set("Select your TM")  # default value
TM_dropdown = OptionMenu(window, TM, *TM_titles)
# return TM_dropdown




# 2. date
cal = Calendar(window)


def select_date():
    selected_date = ''
    date.config(text="Selected Date is: " + cal.get_date())
    selected_date = cal.get_date()
    sd = selected_date.split('/')
    sd = datetime(day=int(sd[1]), month=int(sd[0]), year= int(f'20{sd[2]}'))

    return sd.strftime('%d. %B %Y')
    # return selected_date

date = Label(window, text="")


# 3. gender
m = IntVar()
f = IntVar()
NA = IntVar()


def retrieve_gender():
    result = "male: %d,\nfemale: %d,\nNA: %d" % (m.get(), f.get(), NA.get())
    if m.get() == 1:
        return 'm'
    elif f.get() == 1:
        return 'f'
    elif NA.get() == 1:
        return 'NA'


# 4. name
name_text = tk.Text(window, height=2, width=30, highlightbackground='black')
name_text.insert(tk.END, "")


def retrieve_input(intext):
    input = intext.get("1.0", "end-1c")
    return input


name_submit = Button(window, height=1, width=10, text="Submit",
                     command=lambda: retrieve_input(name_text))


# 5. Subject_topic
subject_topic = tk.Text(window, height=2, width=30, highlightbackground='black')
subject_topic.insert(tk.END, "")

subject_submit = Button(window, height=1, width=10, text="Submit",
                        command=lambda: retrieve_input(subject_topic))


# 6. Case_number
case_num = tk.Text(window, height=2, width=30, highlightbackground='black')
case_num.insert(tk.END, "")

case_submit = Button(window, height=1, width=10, text="Submit",
                     command=lambda: retrieve_input(case_num))


# 7. Porsche Zentrum
#def select_PZ():
PZ_list = pd.read_excel(r"Porsche_Zentren.xlsx")
df = pd.DataFrame(PZ_list)

PZ = StringVar(window)
PZ_titles = get_TM_names_list.get_PZ_list(df)
PZ.set("Select the Porsche Zentrum")  # default value
PZ_dropdown = OptionMenu(window, PZ, *PZ_titles)
# return PZ_dropdown


# 8. Agents_name
agent_name = tk.Text(window, height=2, width=30, highlightbackground='black')
agent_name.insert(tk.END, "")



# Submit all with one Button
input_valuesList = []
def submitAll():
    input_valuesList.append(return_from_dropdown(TM))
    input_valuesList.append(select_date())
    input_valuesList.append(retrieve_gender())
    input_valuesList.append(retrieve_input(name_text))
    input_valuesList.append(retrieve_input(subject_topic))
    input_valuesList.append(retrieve_input(case_num))
    input_valuesList.append(return_from_dropdown(PZ))
    input_valuesList.append(retrieve_input(agent_name))
    return input_valuesList
    # return input_valuesList


submit_all_button = Button(window, height=1, width=20, text="Create Response",
                           command=lambda: submitAll())

# Packing GUI-Screen
Title.pack()

TM_dropdown.pack(side=TOP)
PZ_dropdown.pack(side=TOP)

sep_TM_date.pack(anchor=NE)
cal.pack(side=RIGHT, anchor=NE, pady=20)

date.pack(side=RIGHT, anchor=NE, pady=20)

sep_date_gender.pack()
Checkbutton(window, text="male", variable=m).pack(side=TOP)
Checkbutton(window, text="female", variable=f).pack(side=TOP)
Checkbutton(window, text="N/A", variable=NA).pack(side=TOP)


sep_gender_CustomerName.pack()
name_text.pack()


sep_CustomerName_Subject.pack()
sep_subj.pack()
subject_topic.pack()


sep_subj_case.pack()
case_num.pack()


sep_case_agent.pack()
agent_name.pack()

submit_all_button.pack(side=RIGHT)


# topic, date, gender, name, subject_topic, case, PZ=""
# Extract values needed for Output (Compine all Buttons)



# gender = get_key(1)

# name = input_valuesList[2]


window.mainloop()

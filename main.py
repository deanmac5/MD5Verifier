from tkinter import *
from tkinter import filedialog
import os


def choose_file_a():
    global file_a_filename
    fn = filedialog.askopenfile()
    filename = os.path.basename(fn.name)
    file_a_label.config(text=filename)
    file_a_filename = fn.name
    enable_compare()


def choose_file_b():
    global file_b_filename
    fn = filedialog.askopenfile()
    filename = os.path.basename(fn.name)
    file_b_label.config(text=filename)
    file_b_filename = fn.name
    enable_compare()


def convert_to_dict(line_list):
    result = {}
    for item in line_list:
        val = item.split('  ')
        result[val[1].rstrip()] = val[0].rstrip()
    return result


def compare_pressed():
    with open(file_a_filename) as af:
        a_text = af.readlines()
    with open(file_b_filename) as bf:
        b_text = bf.readlines()
    a_dict = convert_to_dict(a_text)
    b_dict = convert_to_dict(b_text)
    compare_dicts(a_dict, b_dict)


def enable_compare():
    if len(file_a_label.cget("text")) != 0 and len(file_b_label.cget("text")) != 0:
        compare_button.config(state="normal")


def compare_dicts(a_dict, b_dict):
    missing_file = []
    for k in a_dict:
        if k not in b_dict:
            missing_file.add(k)


window = Tk()
window.title("MD5 Verifier")
window.config(padx=50, pady=20)
window.after(1000)

title = Label(text="MD5 Verification Application")
title.grid(row=0, column=1)

file_a_button = Button(text="Choose file A", command=choose_file_a)
file_a_label = Label(text="")
file_a_filename = ""

file_b_button = Button(text="Choose file B", command=choose_file_b)
file_b_label = Label(text="")
file_b_filename = ""

file_a_button.grid(row=1, column=0)
file_a_label.grid(row=1, column=1)
file_b_button.grid(row=2, column=0)
file_b_label.grid(row=2, column=1)

compare_button = Button(text="Compare", state="disabled", command=compare_pressed)
compare_button.grid(row=3, column=1)


window.mainloop()

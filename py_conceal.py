import os
import os.path
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
import webbrowser


root = tk.Tk()
root.geometry("500x300")
root.resizable(False, False)
root.title("PyConceal v2.0.0")
root.config(background="#a30000")

def callback(url):
    webbrowser.open_new_tab(url)

def elements():
    app_banner = Label(root, text="PyConceal",
                        padx=15,
                        pady=15,
                        bg="#a30000",
                        fg="white",
                        font="Magneto 20 bold")
    app_banner.grid(row=1,
                    column=3,
                    pady=10,
                    padx=5,
                    columnspan=3)

    copyright_label = Label(root, text="Copyright © Ashfaaq Rifath - PyConceal",
                        padx=0,
                        pady=0,
                        bg="#a30000",
                        fg="white",)
    copyright_label.grid(row=2,
                    column=3,
                    pady=0,
                    padx=0,
                    columnspan=3)

    hide_button = Button(root,
                        text="Hide files",
                        command=hide_files,
                        width=10,
                        bg="#1fab00",
                        pady=10,
                        padx=15,
                        relief=GROOVE,
                        font="Arial 10")
    hide_button.grid(row=5,
                    column=3,
                    pady=20,
                    padx=20)

    show_button = Button(root,
                        text="Show Files",
                        command=show_files,
                        width=10,
                        bg="#ffc800",
                        pady=10,
                        padx=15,
                        relief=GROOVE,
                        font="Arial 10")
    show_button.grid(row=5,
                    column=5,
                    pady=20,
                    padx=20,)

    password = Entry(root,
                        width=13,
                        textvariable=pass_entry,
                        font="Arial 11")
    password.grid(row=6,
                        column=5,
                        pady=0,
                        padx=0,
                        columnspan=2)

    psswrd = Label(root,
                        text="Password",
                        fg="white", 
                        bg="#a30000",
                        pady=5,
                        padx=5,
                        font="Arial 10")
    psswrd.grid(row=7,
                    column=5,
                    pady=5,
                    padx=5)

    github_link = Label(root, text="GitHub", font="Arial 10", fg="white", bg="#a30000", cursor="hand2")
    github_link.grid(row=6,
                    pady=5,
                    padx=20,
                    column=2,)
    github_link.bind("<Button-1>", lambda e:
    callback("https://github.com/ashfaaqrifath/PyConceal"))


def hide_files():
    #change this file path to the desired file path
    file_exists = os.path.exists('C:/Users/Public/Hidden')
    if file_exists == False:
        os.mkdir("C:/Users/Public/Hidden")

    #change this file path to the desired file path
    os.system("attrib +h /s /d C:/Users/Public/Hidden")
    messagebox.showinfo("Success", "Folder hidden: C:/Users/Public/Hidden")

def show_files():  
    usr_password = pass_entry.get()

    if usr_password == "1234":
        #change this file path to the desired file path
        os.system("attrib -h /s /d C:/Users/Public/Hidden")
        messagebox.showinfo("Success", "Folder visible: C:/Users/Public/Hidden")

    elif usr_password != "1234":
        messagebox.showerror("Invalid password", "Wrong password")

    elif not pass_entry.get():
        messagebox.showerror("Invalid password", "Enter the password")

var = IntVar()
pass_entry = StringVar()
download_path = StringVar()

elements()
root.mainloop()

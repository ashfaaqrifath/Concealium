import os
import os.path
import shutil
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile
from cryptography.fernet import Fernet
from zipfile import ZipFile
import webbrowser


root = tk.Tk()
root.geometry("650x400")
root.resizable(False, False)
root.title("Concealium v3.0.0")
root.config(background="#a30000")

#app icon
# p1 = PhotoImage(file = "concealium.png")
# root.iconphoto(False, p1)

def callback(url):
    webbrowser.open_new_tab(url)

def elements():
    app_banner = Label(root, text="Concealium",
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

    copyright_label = Label(root, text="Copyright © Ashfaaq Rifath - Concealium",
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
                        text="Hide Folder",
                        command=hide_folder,
                        width=10,
                        bg="#ffc800",
                        pady=10,
                        padx=15,
                        relief=GROOVE,
                        font="Arial 10 bold")
    hide_button.grid(row=5,
                    column=3,
                    pady=20,
                    padx=20)

    show_button = Button(root,
                        text="Show Folder",
                        command=show_folder,
                        width=10,
                        bg="#1fab00",
                        pady=10,
                        padx=15,
                        relief=GROOVE,
                        font="Arial 10 bold")
    show_button.grid(row=5,
                    column=4,
                    pady=20,
                    padx=20,)

    encrypt_button = Button(root,
                        text="Encrypt Folder",
                        command=encrypt_folder,
                        width=10,
                        bg="#ffc800",
                        pady=10,
                        padx=15,
                        relief=GROOVE,
                        font="Arial 10 bold")
    encrypt_button.grid(row=6,
                    column=3,
                    pady=20,
                    padx=20,)

    decrypt_button = Button(root,
                        text="Decrypt Folder",
                        command=decrypt_folder,
                        width=10,
                        bg="#1fab00",
                        pady=10,
                        padx=15,
                        relief=GROOVE,
                        font="Arial 10 bold")
    decrypt_button.grid(row=7,
                    column=3,
                    pady=20,
                    padx=20,)

    zip_button = Button(root,
                        text="Zip Folder",
                        command=zip_folder,
                        width=10,
                        bg="#ffc800",
                        pady=10,
                        padx=15,
                        relief=GROOVE,
                        font="Arial 10 bold")
    zip_button.grid(row=5,
                    column=5,
                    pady=20,
                    padx=20,)

    unzip_button = Button(root,
                        text="Unzip Folder",
                        command=unzip_folder,
                        width=10,
                        bg="#1fab00",
                        pady=10,
                        padx=15,
                        relief=GROOVE,
                        font="Arial 10 bold")
    unzip_button.grid(row=6,
                    column=5,
                    pady=20,
                    padx=20,)

    make_folder = Button(root,
                        text="Make Folder",
                        command=the_folder,
                        width=10,
                        bg="#ffc800",
                        pady=10,
                        padx=15,
                        relief=GROOVE,
                        font="Arial 10 bold")
    make_folder.grid(row=7,
                    column=5,
                    pady=20,
                    padx=20,)

    github_link = Label(root, text="GitHub", font="Arial 10", fg="white", bg="#a30000", cursor="hand2")
    github_link.grid(row=8,
                    pady=5,
                    padx=20,
                    column=2,)
    github_link.bind("<Button-1>", lambda e:
    callback("https://github.com/ashfaaqrifath/Concealium"))


save_path = "C:/Users/Public"
zip_file = "C:/Users/Public/Hidden"

zip_save = os.path.join(save_path, "Hidden")
key_path = os.path.join(save_path, "encryption.key")


def zip_folder():
    try:
        shutil.make_archive(zip_save, 'zip', zip_file)
        shutil.rmtree("C:/Users/Public/Hidden")
        messagebox.showinfo("Success", "Folder zipped: C:/Users/Public/Hidden.zip")
    except FileNotFoundError:
        messagebox.showerror("Error", "Folder already zipped")

def unzip_folder():
    try:
        zipped_folder = "C:/Users/Public/Hidden.zip"
        with ZipFile(zipped_folder, 'r') as zip:
            zip.extractall("C:/Users/Public/Hidden")
        os.remove(zipped_folder)
        messagebox.showinfo("Success", "Folder unzipped: C:/Users/Public/Hidden")
    except FileNotFoundError:
        messagebox.showerror("Error", "Folder already unzipped")

def encrypt_folder():
    try:
        confirm = messagebox.askquestion('Encrypt Folder', 'Do you want to encrypt the Hidden folder ?')

        if confirm == 'yes' :
            shutil.make_archive(zip_save, 'zip', zip_file)
            shutil.rmtree("C:/Users/Public/Hidden")

            key = Fernet.generate_key()
            with open(key_path, "wb") as encryptkey:
                encryptkey.write(key)
            fernet = Fernet(key)

            user_file_encp = "C:/Users/Public/Hidden.zip"

            with open(user_file_encp, 'rb') as file:
                    original_file = file.read()
            encrypt = fernet.encrypt(original_file)

            with open(user_file_encp, 'wb') as encp_file:
                encp_file.write(encrypt)
            messagebox.showinfo("Encrypted", "Folder encrypted. DO NOT DELETE THE ENCRYPTION KEY")
        else :
            pass

    except FileNotFoundError:
        messagebox.showerror("Error", "Folder already encrypted")

def decryption():
    try:
        usr_password = pass_entry2.get()

        if usr_password == "":
            pass
        
        #this is the password. this can be changed in the source code.
        elif usr_password == "1234":
            user_file_decp = "C:/Users/Public/Hidden.zip"

            with open(key_path, 'rb') as encp_key:
                read_enc_key = encp_key.read()

            fernet = Fernet(read_enc_key)

            with open(user_file_decp, 'rb') as read_encp_file:
                encrypted_file  = read_encp_file.read()
        
            decrypt = fernet.decrypt(encrypted_file)

            with open(user_file_decp, 'wb') as decp_file:
                decp_file.write(decrypt)

            with ZipFile(user_file_decp, 'r') as zip:
                zip.extractall("C:/Users/Public/Hidden")

            os.remove(user_file_decp)
            messagebox.showinfo("Decrypted", "Folder decrypted: C:/Users/Public/Hidden")

        elif usr_password != "1234":
            messagebox.showerror("Invalid password", "Wrong password")

        elif not pass_entry.get():
            messagebox.showerror("Invalid password", "Enter the password")

    except FileNotFoundError:
        messagebox.showerror("Error", "Folder already decrypted")

def decrypt_folder():
    password2 = Entry(root,
                        width=13,
                        textvariable=pass_entry2,
                        font="Arial 11")
    password2.grid(row=7,
                        column=4,
                        pady=0,
                        padx=0,
                        columnspan=1)

    decrypt_button2 = Button(root,
                        text="Enter Password",
                        command=decryption,
                        width=10,
                        bg="#56abf0",
                        pady=10,
                        padx=15,
                        relief=GROOVE,
                        font="Arial 10")
    decrypt_button2.grid(row=7,
                    column=3,
                    pady=20,
                    padx=20,)

def the_folder():
    file_exists = os.path.exists('C:/Users/Public/Hidden')
    if file_exists == False:
        os.mkdir("C:/Users/Public/Hidden")
        messagebox.showinfo("Folder Created", "Hidden folder created: C:/Users/Public/Hidden")
    else:
        messagebox.showinfo("Folder Exists", "Folder already exists: C:/Users/Public/Hidden")

def hide_folder():
    #change this file path to the desired file path
    file_exists = os.path.exists('C:/Users/Public/Hidden')
    if file_exists == False:
        os.mkdir("C:/Users/Public/Hidden")

    file_exists = os.path.exists('C:/Users/Public/Hidden.zip')
    if file_exists == True:
        os.system("attrib +h /s /d C:/Users/Public/Hidden.zip")

    #change this file path to the desired file path
    os.system("attrib +h /s /d C:/Users/Public/Hidden")
    messagebox.showinfo("Success", "Folder hidden: C:/Users/Public/Hidden")

def show_folder():
    password = Entry(root,
                        width=13,
                        textvariable=pass_entry,
                        font="Arial 11")
    password.grid(row=6,
                        column=4,
                        pady=0,
                        padx=0,
                        columnspan=1)

    show_button2 = Button(root,
                        text="Enter Password",
                        command=show_folder,
                        width=10,
                        bg="#56abf0",
                        pady=10,
                        padx=15,
                        relief=GROOVE,
                        font="Arial 10")
    show_button2.grid(row=5,
                    column=4,
                    pady=20,
                    padx=20,)

    usr_password = pass_entry.get()

    if usr_password == "":
        pass
    
    #this is the password. this can be changed in the source code.
    elif usr_password == "1234":
        file_exists = os.path.exists('C:/Users/Public/Hidden.zip')
        if file_exists == True:
            os.system("attrib -h /s /d C:/Users/Public/Hidden.zip")

        #change this file path to the desired file path
        os.system("attrib -h /s /d C:/Users/Public/Hidden")
        messagebox.showinfo("Success", "Folder visible: C:/Users/Public/Hidden")

    elif usr_password != "1234":
        messagebox.showerror("Invalid password", "Wrong password")

    elif not pass_entry.get():
        messagebox.showerror("Invalid password", "Enter the password")



var = IntVar()
pass_entry = StringVar()
pass_entry2 = StringVar()

elements()
root.mainloop()



# <<< Copyright (c) 2022 Ashfaaq Rifath - Concealium v3.0.0>>>

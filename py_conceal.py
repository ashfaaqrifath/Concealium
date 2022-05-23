import os
from time import sleep

hide_files = input("Hide files or Show hidden files (h/s): ")

if hide_files == "h":
    os.system("attrib +h /s /d")
    print("Your files are hidden.")
    sleep(2)

elif hide_files == "s":
    usr_password = input("Enter password: ")
    if usr_password == "1234":
        os.system("attrib -h /s /d")
        print("Your files are visible.")
        sleep(2)
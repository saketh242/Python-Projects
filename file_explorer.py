"""
A simple file explorer program that takes the file or directory name from user and opens it
Uses python builtin OS Module
"""

import os
print("home dir is " + os.path.expanduser('~'))
def file_explorer():
    
    while True:
        input_search = input("What are you searching file or folder?: ")
        if input_search not in "file, folder":
            continue
        else:
            break
    if input_search == "file":
        input_name = input("Enter the file name: ")
    else:
        input_name = input("Enter the folder name: ")

    home_dir = os.path.expanduser('~')
    
    close = False
    for folder, sub_folders, files in os.walk(home_dir):

        if input_search == "folder":
            for sub_fold in sub_folders:
                if input_name in sub_fold:
                    print(folder+ "\\" + sub_fold)
                    k = open_file(folder,input_name)
                    if not k:
                        close = True
                        break

        if input_search == "file":
            for file in files:
                if input_name in file:
                    print(folder + "\\" + file)
                    k = open_file(folder,input_name)
                    if not k:
                        close = True
                        break
        if close:
            break
        else:
            pass    

def open_file(folder,file):
    try:
        os.startfile(folder+ "\\" + file)
    except OSError:
        print("File dependencies not satisfied!!!")
        return False
    else:
        return True
            
        
file_explorer()

# Contact
# sp357@njit.edu

import os

def rename_files():
    #get file names from a given folder
    file_list = os.listdir(r"C:\Users\Ian Skyles\Documents\GitHub\ud036\LessonOne_UseFunctions\rename_files\secretMessageUnEncrypted")
    print(file_list)

    
    #check current directory
    #print(os.getcwd())

    #change the current directory to the one with the pictures
    os.chdir(r"C:\Users\Ian Skyles\Documents\GitHub\ud036\LessonOne_UseFunctions\rename_files\secretMessageUnEncrypted")
    
    #rename all of  the files/photos
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))

rename_files()

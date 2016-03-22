
import urllib

def read_text():
    documentToCheck = open("C:\Users\Ian Skyles\Documents\GitHub\ud036\LessonTwo_UseClasses\PartThree_ProfanityEditor\movie_quotes_d.txt")
    contents_of_document = documentToCheck.read()
    #print(contents_of_document)
    documentToCheck.close()
    check_profanity(contents_of_document)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Profanity altert!!!")
    elif "false" in output:
        print("This document has no curse words.")
    else:
        print("Could not scan the document properly")


read_text()


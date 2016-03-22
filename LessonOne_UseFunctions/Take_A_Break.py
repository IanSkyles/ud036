import webbrowser
import time

breakCount = 0
totalBreaks = 3

print("This program started at " + time.ctime())
while breakCount < totalBreaks:
    time.sleep(3)
    webbrowser.open("http://youtube.com/")
    breakCount = breakCount + 1

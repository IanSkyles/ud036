import webbrowser
import time

breakCount = 0

print("This program started at " + time.ctime())
while breakCount < 3:
    time.sleep(3)
    webbrowser.open("http://youtube.com/")
    breakCount = breakCount + 1

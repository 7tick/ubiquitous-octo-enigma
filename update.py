#!/usr/bin/python
import time
import webbrowser
import random
i = 0
while i < 3:
    randomTime = random.randint(10, 20)
    print (str(randomTime))
    time.sleep(randomTime * 60)
    webbrowser.open("https://www.tomorrowtides.com/rickrolled85.html")
    i = i + 1

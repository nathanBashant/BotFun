
import pyautogui as pg
import time
import random

url = input("Enter URL: ")
t = int(input("Enter Time Duration in Minutes: "))
T = 60*t
n = int(input("Enter Number of Times: "))

#pg.hotkey('win','2') # 2 refers to the position of desired Tor browser in taskbar
for i in range(n):
    pg.hotkey('win','2') #opens second slot on task bar
    time.sleep(1)
    pg.hotkey('ctrl','shift','n')
    time.sleep(1) #rests for 1 second
    pg.typewrite(url) #types in url
    pg.hotkey('enter') #presses enter
    time.sleep(5) #sleeps for 5 seconds
    ti = random.randint(0,T) # creates a uniques watch time to make it safer to be detected(Just in case) 
    print(ti) #prints the unique time
    time.sleep(ti) #sleeps for the watch time
    pg.hotkey('ctrl','w')
    time.sleep(1)
    pg.hotkey('ctrl','w') #closes chrome
    time.sleep(0.5) #waits and then starts over
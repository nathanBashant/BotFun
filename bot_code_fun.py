import pyautogui as pg
import time
import random

'''
url = input("Enter URL: ")
t = int(input("Enter Time Duration in Minutes(only): "))
T = 60*t
n = int(input("Enter Number of Times To Watch: "))

pg.hotkey('win','6') # 2 refers to the position of desired Tor browser in taskbar
for i in range(n):
    time.sleep(10)
    pg.typewrite(url)
    pg.hotkey('enter')
    time.sleep(5)
    ti = random.randint(0,T) # creates a uniques watch time to make it safer to be detected(Just in case) 
    print(ti)
    time.sleep(ti)
    pg.hotkey('ctrl','w')
    time.sleep(0.5)

'''


url = "https://soundcloud.com/"
n = int(input("Enter Number of Times: "))
example = "fullacclog1@gmail.com"
password = "gokarts19"
example2 = "nagelthebagel1@gmail.com"
ti = random.randint(21,42)
x1 = 1506
y1 = 217

x2 = 1017
y2 = 359

x3_age = 932
y3_age = 490

x4_gen = 934
y4_gen = 574

x5_gen_choice = 819
y5_gen_choice = 645

#SIGN UP ONLY FOR SOUNDCLOUD WHATEVER EMAIL
#notes:store email and pass for all soundcloud accounts
#create thousands of google accounts and make them all do different things
#train bots and age them to create and army

#idea: gmail bot that sends myself and email of whatever photo,pdf,etc. is needed



#idea: have multiple bots try to gain social media following and then have my bots promote their stuff
#and they all grow anyways
#visual:      social media bot (1000 followers) ----- social media bot (1000 followers)
#                            /                                  \
#        my other bots feeding smb + organic growth    my other bots feeding smb + organic growth


for i in range(n):
    time.sleep(1)
    pg.hotkey('win','3')
    time.sleep(0.5)
    pg.hotkey('ctrl','shift','n')
    time.sleep(1)
    pg.typewrite(url)
    pg.hotkey('enter')
    time.sleep(3)

    pg.moveTo(x1,y1)
    pg.click()

    time.sleep(2)

    pg.moveTo(x2,y2)
    pg.click()

    time.sleep(3)

    pg.typewrite(example2)
    pg.hotkey('enter')

    time.sleep(2)

    pg.typewrite(password)
    pg.hotkey('enter')

    time.sleep(5)

    pg.moveTo(x3_age,y3_age)
    pg.click()
    pg.typewrite("25")

    time.sleep(1) #rest after age done

    pg.moveTo(x4_gen,y4_gen) #mouse to gender box
    time.sleep(1) #rests at gender box
    pg.leftClick() #clicks gender box
    time.sleep(2) #rests after clicking gender box
    pg.moveTo(x5_gen_choice,y5_gen_choice) #moves to female option
    time.sleep(5) #rests on option
    pg.leftClick() #clicks female

    time.sleep(1)

    pg.leftClick() #clicks continue

    time.sleep(100)

    pg.hotkey('ctrl','w')
    time.sleep(2)
    pg.hotkey('ctrl','w')
    

'''
#pg.mouseInfo()
#link
378
871

#create
243
576

#first
662
419

#last
841
427

#user
677
480

#pass
640
609

832
608

#next
910
772

#month
656
609

657
716

#day
767
614

#year
889
615

#gender
750
692

749
745

#scroll all the way down

#agree
895
893

'''
import pyautogui as pg
import time
import random
import pandas as pd
import csv

acc_df = pd.read_csv("gmail_account_sheet.csv")
n = int(input("Enter Number of Times: "))
search_text1 = "https://account.proton.me/signup"
password = "gokarts19?"
email = "nathanbashant19@gmail.com"

name_col = pd.Series(acc_df["first name"])
lastn_col = pd.Series(acc_df["last name"])
user_col = pd.Series(acc_df["username"])
rand_num = random.randint(0,len(user_col))
user_rand = random.randint(10000,11000)

x_user_box = 928
y_user_box = 381

x_pro_pass = 943
y_pro_pass = 474

x_pro_pass2 = 795
y_pro_pass2 = 571

x_button = 953
y_button = 659

#cont free
x_free = 690
y_free = 468
#capt
x_cap = 801
y_cap = 451
#next
x_nbu = 950
y_nbu = 544
#phone no
x_ph = 955
y_ph = 635
#conf
x_con = 956
y_con = 601

#mailbox link
x_mailink = 927
y_mailink = 371

x_e = 1053
y_e = 329

x_get = 941
y_get = 563

x_ref = 157
y_ref = 227
    #click first e
x_fe = 545
y_fe = 254
    #dub click
x_dub = 368
y_dub = 364

x_vbox = 854
y_vbox = 446

x_vbut = 957
y_vbut = 530

x_bruh = 281
y_bruh = 261

x_tr = 428
y_tr = 157

################################################

x_first = 692
y_first = 419

x_last = 841
y_last = 427

x_user = 758
y_user = 482

x_passw = 640
y_passw = 609

x_passwCONF = 832
y_passwCONF = 608

x_nxt = 910
y_nxt = 772

x_del = 846
y_del = 440

#note: must use adelaide vpn and internet explorer for google account production
#requirements: internet explorer, Adelaide/remote vpn, center monitor
#proton accounts turned into google accounts
#print(name_col[rand_num] + lastn_col[rand_num] + str(user_rand))

my_list = []

for i in range(n):
    username_actual = name_col[rand_num] + lastn_col[rand_num] + str(user_rand)

    pg.hotkey('win','2')

    time.sleep(1)
    
    pg.typewrite(search_text1)
    pg.hotkey('enter')
    
    time.sleep(5)

    pg.moveTo(x_user_box,y_user_box)
    pg.leftClick()
    pg.typewrite(username_actual)

    pg.moveTo(x_pro_pass,y_pro_pass)
    pg.leftClick()
    pg.typewrite(password)

    pg.moveTo(x_pro_pass2,y_pro_pass2)
    pg.leftClick()
    pg.typewrite(password)

    pg.moveTo(x_button,y_button)
    pg.leftClick()

    time.sleep(3)

    pg.moveTo(x_free,y_free)
    pg.leftClick()

    time.sleep(3)

    pg.moveTo(x_e,y_e)
    pg.leftClick()
    pg.typewrite(email)

    time.sleep(1)

    pg.moveTo(x_get,y_get)
    pg.leftClick()

    time.sleep(3)

    pg.hotkey('ctrl','n')
    pg.typewrite("https://mail.google.com/mail/u/3/?ogbl#inbox")
    pg.hotkey('enter')
    time.sleep(3)
    
    pg.moveTo(x_bruh,y_bruh)
    pg.leftClick()
    pg.moveTo(x_tr,y_tr)
    pg.leftClick()

    time.sleep(2)

    pg.moveTo(x_ref,y_ref)
    pg.leftClick()
    time.sleep(1)
    pg.leftClick()
    time.sleep(1)
    pg.leftClick()
    time.sleep(1)
    pg.leftClick()

    time.sleep(7)

    pg.moveTo(x_fe,y_fe)
    pg.leftClick()

    time.sleep(2)

    pg.moveTo(x_dub,y_dub)
    pg.doubleClick()
    pg.hotkey('ctrl','c')
    pg.hotkey('ctrl','w')

    pg.moveTo(x_vbox,y_vbox)
    pg.leftClick()
    pg.hotkey('ctrl','v')
    pg.moveTo(x_vbut,y_vbut)
    pg.leftClick()

    my_list.append(username_actual)


    '''
    pg.hotkey('win','9') 

    time.sleep(1)
    
    #pg.typewrite(search_text)
    pg.hotkey('enter')
    
    time.sleep(2)

    pg.moveTo(x_first,y_first)
    pg.leftClick()
    pg.typewrite(name_col[rand_num])

    pg.moveTo(x_last,y_last)
    pg.leftClick()
    pg.typewrite(lastn_col[rand_num])

    time.sleep(1)

    pg.moveTo(x_user,y_user)
    pg.leftClick()

    pg.typewrite(username_actual,interval=0.01)
    my_list.append(username_actual)

    pg.moveTo(x_del,y_del)
    pg.tripleClick()
    pg.hotkey('delete')
    pg.typewrite(username_actual)

    time.sleep(1)

    pg.moveTo(x_passw,y_passw)
    pg.leftClick()
    pg.typewrite(password)

    pg.moveTo(x_passwCONF,y_passwCONF)
    pg.leftClick()
    pg.typewrite(password)

    pg.moveTo(x_nxt,y_nxt)
    pg.leftClick()

    time.sleep(100000)

    pg.hotkey('ctrl','w')
    time.sleep(1)
    pg.hotkey('ctrl','w') 
    time.sleep(0.5) 
    print(my_list)
    '''

    with open('email_data.csv', 'w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(my_list)


#pg.locateOnScreen('signinbuttongoogle.png')
'''
'''
#pg.mouseInfo()
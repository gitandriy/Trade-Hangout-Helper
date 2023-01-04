import time 
import pynput
from pynput.keyboard import Key, Controller

keyboard = Controller()

sentsofar = 0
print("Welcome to Trade Hangout Helper! (or THH for short!) ")
time.sleep(4)
print(" ")
print("-------Type 1, 2 or 3 to select one of the premade messages, or type 4 for your own custom message!-------")
print(" ")
print("Send Trades! I am AFK and will Accept or Counter! [1]")
print("AFK Downgrading! I will Accept or Counter!        [2]")
print("AFK Upgrading! I will Accept or Counter!          [3]")
print("*Type your own message*                           [4]")

option1 = "Send Trades! I am AFK and will Accept or Counter!"
option2 = "AFK Downgrading! I will Accept or Counter!"
option3 = "AFK Upgrading! I will Accept or Counter!"
userchoice = input("Option: ")

if userchoice == '4':
    customchat = input("What should the message say? ")

repeattimes = int(input("How many times should the message be sent? "))
loopdelaytime = float(input("How long should the delay between messages be? (the recommended time is 25 seconds ) "))


print("In 20 seconds, messages will start being sent. Please make sure you are in trade hangout and that it is fullscreen.")
time.sleep(20)
for i in range(0, repeattimes):
    if userchoice == "1":
        keyboard.press('/')
        keyboard.release('/')
        time.sleep(1)
        keyboard.type(option1)
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        sentsofar = sentsofar + 1
        msgsentmsg = str(sentsofar) + " messages sent!"
        print(msgsentmsg)
        time.sleep(loopdelaytime)
    if userchoice == '2':
        keyboard.press('/')
        keyboard.release('/')
        time.sleep(1)
        keyboard.type(option2)
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        sentsofar = sentsofar + 1
        msgsentmsg = str(sentsofar) + " messages sent!"
        print(msgsentmsg)
        time.sleep(loopdelaytime)
    if userchoice == '3':
        keyboard.press('/')
        keyboard.release('/')
        time.sleep(1)
        keyboard.type(option3)
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        sentsofar = sentsofar + 1
        msgsentmsg = str(sentsofar) + " messages sent!"
        print(msgsentmsg)
        time.sleep(loopdelaytime)
    if userchoice == '4':
        keyboard.press('/')
        keyboard.release('/')
        time.sleep(1)
        keyboard.type(customchat)
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        sentsofar = sentsofar + 1
        msgsentmsg = str(sentsofar) + " messages sent!"
        print(msgsentmsg)
        time.sleep(loopdelaytime)




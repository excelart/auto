import virtkey
from time import sleep

v = virtkey.virtkey()
sleep(3)



for i in range(0,5):
    v.press_keysym(0xff54) # down
    v.release_keysym(0xff54)
    for ii in range(0,10):
        pass
    v.press_keysym(0xffc1) # F4
    v.release_keysym(0xffc1)
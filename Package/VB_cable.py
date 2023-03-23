import os
import time
from pygame import mixer

def V_B():
    mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')
    mixer.music.load("voice.wav")
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(0.1)
    mixer.quit()
    os.remove("voice.wav")

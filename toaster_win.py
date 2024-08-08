from winotify import Notification, audio
import os

def toaster(title, msg):
    toast = Notification(app_id="LittleOwl",
                         title=title,
                         msg=msg,
                         duration="long")
    
    toast.set_audio(audio.LoopingAlarm4, loop=True)
    toast.show()

